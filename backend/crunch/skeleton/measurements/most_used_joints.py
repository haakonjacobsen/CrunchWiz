from crunch.skeleton.measurements.helpers import norm_by_array


def most_used_joints(pos):
    """Calculating the norms. And check for the highest
    value to output the according most used joint.

    :param pos: positions of each joint
    :type pos: list of list of tuples
    :return: index of most used joint
    :rtype: int
    """
    used_list = []
    for i in range(len(pos) - 1):
        joint_Nr = 0
        highest = 0
        total = 0
        for j in range(len(pos[i])):
            used = norm_by_array(pos[i][j], pos[i + 1][j])
            if highest <= used:
                highest = used
                joint_Nr = j
            total += used
        total = total / 24
        used_list.append((joint_Nr, round(total, 6)))

    most_used = max(used_list, key=lambda x: x[1])[0]
    joint_map = ["Nose",
                 "Neck",
                 "Right Shoulder",
                 "Right Elbow",
                 "Right Wrist",
                 "Left Shoulder",
                 "Left Elbow",
                 "Left Wrist",
                 "MidHip",
                 "Right Hip",
                 "Right Knee",
                 "Right Ankle",
                 "Left Hip",
                 "Left Knee",
                 "Left Ankle",
                 "Right Eye",
                 "Left Eye",
                 "Right Ear",
                 "Left Ear",
                 "Left BigToe",
                 "Left SmallToe",
                 "Left Heel",
                 "Right BigToe",
                 "Right SmallToe",
                 "Right Heel"
                 ]
    return joint_map[most_used]
