from loguru import logger

def cal(N, bridges):
    mod = 10**9 + 7
    bw_list = [[1,1] for _ in range(N+1)]
    con_list = [[] for _ in range(N+1)]
    root = bridges[0][0]

    def update(cur, parent):
        logger.debug(cur)
        for child in con_list[cur]:
            if child == parent:
                continue
            else:
                update(child, cur)
            # enter here if children all updated
            for child in con_list[cur]:
                # black
                bw_list[cur][0] *= bw_list[child][1] % mod
                # white
                bw_list[cur][1] *= (bw_list[child][0] + bw_list[child][1]) % mod
    update(root, 0)
    logger.debug(bw_list)

    return sum(bw_list[root])



def test_sample1():
    N = 5
    bridges = [
            [2, 5],
            [1, 5],
            [2, 4],
            [3, 2]
            ]
    assert  14 == cal(N, bridges)

def test_sample2():
    N = 10
    bridges = [
            [7, 9],
            [8, 1],
            [9, 6],
            [10, 8],
            [8, 6],
            [10, 3],
            [5, 8],
            [4, 8],
            [2, 5],
            ]
    assert  192 == cal(N, bridges)
