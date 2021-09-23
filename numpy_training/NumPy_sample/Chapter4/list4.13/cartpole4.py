# coding: utf-8
import gym # gymとNumPyのインポート
import numpy as np

# 環境に相当するオブジェクトをenvとおく
env = gym.make('CartPole-v0')

# 195ステップ連続でポールが倒れないことを目指す
goal_average_steps = 195
# 最大ステップ数
max_number_of_steps = 200
# 評価の範囲のエピソード数
num_consecutive_iterations = 100
num_episodes = 5000
last_time_steps = np.zeros(num_consecutive_iterations)

# 価値関数の値を保存するテーブルを作成する
# np.random.uniformは指定された範囲での一様乱数を返す
q_table = np.random.uniform(low=-1, high=1, size=(4**4, env.action_space.n))

def bins(clip_min, clip_max, num):
    # np.linspaceは指定された範囲における等間隔数列を返す
    return np.linspace(clip_min, clip_max, num + 1)[1:-1]

def digitize_state(observation):
    # 各値を4個の離散値に変換
    # np.digitizeは与えられた値をbinsで指定した基数に当てはめる関数。インデックスを返す
    cart_pos, cart_v, pole_angle, pole_v=observation
    digitized = [np.digitize(cart_pos, bins=bins(-2.4, 2.4, 4)),
                 np.digitize(cart_v, bins=bins(-3.0, 3.0, 4)),
                 np.digitize(pole_angle, bins=bins(-0.5, 0.5, 4)),
                 np.digitize(pole_v, bins=bins(-2.0, 2.0, 4))]
    # 0～255に変換

    # インデックス付きループをすることができる
    return sum([x* (4**i) for i, x in enumerate(digitized)])

def get_action(state, action, observation, reward, episode):
    next_state = digitize_state(observation)

    epsilon = 0.5 * (0.99** episode)
    if epsilon <= np.random.uniform(0, 1):
        # q_tableの中で次にとりうる行動の中で最も価値の高いものをnext_actionに格納する
        next_action = np.argmax(q_table[next_state])
    else:
    # そうでなければ20%の確率でランダムな行動をとる
        next_action = np.random.choice([0, 1])


    # Qテーブルの更新
    alpha = 0.2
    gamma = 0.99
    q_table[state, action] = (1 - alpha) * q_table[state, action] + \
        alpha * (reward + gamma * q_table[next_state, next_action])
    return next_action, next_state

step_list = []
for episode in range(num_episodes):
    # 環境の初期化
    observation = env.reset()

    state = digitize_state(observation)
    action = np.argmax(q_table[state])

    episode_reward = 0
    for t in range(max_number_of_steps):
        # CartPoleの描画
        env.render()

        # actionをとった時の環境、報酬、状態が終わったかどうか、デバッグに有益な情報
        observation, reward, done, info=env.step(action)
        # 倒れた時罰則を追加する
        if done:
            reward -= 200
        # 行動の選択
        action, state = get_action(state, action, observation, reward, episode)
        episode_reward += reward

        if done:
            print('%d Episode finished after %f time steps / mean %f' %(episode, t + 1, last_time_steps.mean()))
            last_time_steps = np.hstack((last_time_steps[1:], [t+1]))
            # 継続したステップ数をステップのリストの最後に加える。np.hstack関数は配列をつなげる関数
            step_list.append(last_time_steps.mean())
            break
    # 直近の100エピソードの平均が195以上であれば成功
    if (last_time_steps.mean() >= goal_average_steps):
        print('Episode %d train agent successfully!' % episode)
        break

# 以下のコードでグラフを表示
import matplotlib.pyplot as plt
plt.plot(step_list)
plt.xlabel('episode')
plt.ylabel('mean_step')
plt.show()