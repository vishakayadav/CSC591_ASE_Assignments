import sys

from HW5.test.test_examples import *


def settings(pstr):
    table = {}
    pattern = """\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"""
    r = re.compile(pattern)
    matches = r.findall(pstr)
    for k, v in matches:
        table[k] = coerce(v)
    return table


def cli(options):
    for key, val in options.items():
        val = str(val)
        for n, x in enumerate(sys.argv):
            if x == "-" + key[0] or x == "--" + key:
                if val.lower() == 'false':
                    val = 'true'
                elif val.lower() == 'true':
                    val = 'false'
                else:
                    val = sys.argv[n + 1]
                # val = val == "false" and "true" or val == "true" and "false" or sys.argv[n+1]
        options[key] = coerce(val)
    return options


def main():
    saved, fails, options = {}, 0, the
    for key, val in cli(settings(help_string)).items():
        options[key] = val
        saved[key] = val

    if options["help"]:
        print(help_string)
    else:
        for what, fun in example_funcs.items():
            if options["go"] == "all" or what == options["go"]:
                for k, v in saved.items():
                    options[k] = v
                global seed
                seed = options["seed"]
                if example_funcs[what]() == False:
                    fails += 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)

    sys.exit(fails)


if __name__ == '__main__':
    example('the', 'show settings', test_the)
    example('rand', 'demo random number generation', test_rand)
    example('some', 'demo random number generation', test_some)
    example("nums", "demo of NUM", test_nums)
    example('syms', 'demo SYMS', test_sym)
    example('csv', 'reading csv files', test_csv)
    example('data', 'showing data sets', test_data)
    example('clone', 'replicate structure of a DATA', test_clone)
    example('cliffs', 'stats tests', test_cliffs)
    example('dist', 'distance test', test_dist)
    example('half', 'divide data in halg', test_half)
    example('tree', 'make snd show tree of clusters', test_tree)
    example('sway', 'optimizing', test_sway)
    example('bins', 'find deltas between best and rest', test_bins)
    main()
