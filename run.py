# encoding: utf-8
# @Time : 2021/11/29 10:37 
# @Author : LJtion
# @File : run.py 
# @Software: PyCharm
from maze_env import Maze
from RL_brain import QLearningTable, SarsaTable
import pandas as pd

def update():
    #设置步数
    step_num = 0
    # 跟着行为轨迹
    df = pd.DataFrame(columns=('state','action_space','reward','Q','action'))
    # 转换为迷宫坐标（x,y）改为二维矩阵坐标，易于直接在表格上表达；
    def set_state(observation):
        p = []
        p.append(int((observation[0]-5)/40))
        p.append(int((observation[1]-5)/40))
        # return observation
        return p
    for episode in range(100):
        # initial observation
        observation = env.reset()
        observation = set_state(observation)
        # RL choose action based on observation
        action = RL.choose_action(str(observation))
        while True:
            # fresh env
            env.render()

            # RL take action and get next observation and reward 得到反馈
            observation_, reward, done = env.step(action)

            if observation_ != 'terminal':
                observation_ = set_state(observation_)

            step_num += 1
            print('step:', step_num, 'reward:', reward, 'oboservation', observation_)
            # 根据observation选择action
            # RL choose action based on next observation
            action_ = RL.choose_action(str(observation_))

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_), action_)

            q = RL.q_table.loc[str(observation), action]
            df = df.append(pd.DataFrame({'state': [observation], 'action_space': [env.action_space[action]], 'reward': [reward], 'Q': [q], 'action': action}), ignore_index=True)


            # swap observation估计的动作直接是下一步要进行的动作
            observation = observation_
            action = action_
            # break while loop when end of this episode如果获得完成的标志位
            if done:
                break

    # end of game
    print('game over', step_num)
    df.to_csv('saction3.csv')
    RL.q_table.to_csv('sq_table3.csv')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    # RL = QLearningTable(actions=list(range(env.n_actions)))
    RL = SarsaTable(actions=list(range(env.n_actions)))
    env.after(1, update)
    env.mainloop()