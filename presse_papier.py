def followingIntegers(nbs):
    r = []
    for i, l in enumerate(nbs):
        if not r:
            r.append([])
        for n, li in enumerate(l):
            if not r[-1]:
                r[-1].append(li)
            else:
                if li == nbs[i][n-1] + 1:
                    r[-1].append(li)
                else:
                    r.append([li])
    return sorted(r,
                  key=lambda x: len(x),
                  reverse=True)



def reciepe_details(data):
    if sum(data[0]) / len(data[0]) < sum(data[1]) / len(data[1]):
        return (data[0], data[1])
    else:
        return (data[1], data[0])


def similarities(self, itv_size=20):
    x = self.get_data()["x"]
    intervals = []
    results = []
    for i, p in enumerate(x):
        if not intervals:
            intervals.append(((p - itv_size, p + itv_size)))
            results.append([i])
        else:
            inInterval = False
            for b, itv in enumerate(intervals):
                if p >= itv[0] and p <= itv[1]:
                    results[b].append(i)
                    inInterval = True
            if not inInterval:
                intervals.append(((p - itv_size, p + itv_size)))
                results.append([i])
    return sorted(results,
                  key=lambda x: len(x),
                  reverse=True)