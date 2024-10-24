#!/usr/bin/python3
""" log parsing """

import sys

if __name__ == '__main__':

    fsize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(fsize))
        for key, value in sorted(stats.items()):
            if value:
                print("{}: {}".format(key, value))

    try:
        for l in sys.stdin:
            count += 1
            data = l.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                fsize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, fsize)
        print_stats(stats, fsize)
    except KeyboardInterrupt:
        print_stats(stats, fsize)
        raise
