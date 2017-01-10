import svn.remote
import argparse


# r = svn.remote.RemoteClient(
#     'http://svn.proddev.cccis.com:8090/svn/QA/trunk/acceptance-projects/')
# for dir in r.list():
#     print(dir)
test_category_options = ['AWSQASmokeTest', 'AWSRegression', 'QASmokeTest', 'QARegression', 'CTSmoke', 'ProdSmoke' ]

parser = argparse.ArgumentParser()

parser.add_argument('--select', action='append', dest='acceptance_modules_collection',
                    default=[],
                    help='Select the acceptance test module(s)',
                    required=True
                    )

parser.add_argument('--category', action='store',
                    dest='test_category',
                    help='Specify the test category. Available options: {}'.format(test_category_options),
                    required=True)

parser.add_argument('-c', action='store_const',
                    dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

parser.add_argument('-t', action='store_true',
                    default=False,
                    dest='boolean_t',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false',
                    default=True,
                    dest='boolean_f',
                    help='Set a switch to false')

parser.add_argument('-A', action='append_const',
                    dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const',
                    dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')

parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0')


results = parser.parse_args()
print('test_category     = {!r}'.format(results.test_category))
print('constant_value   = {!r}'.format(results.constant_value))
print('boolean_t        = {!r}'.format(results.boolean_t))
print('boolean_f        = {!r}'.format(results.boolean_f))
print('acceptance_modules_collection       = {!r}'.format(results.acceptance_modules_collection))
print('const_collection = {!r}'.format(results.const_collection))

if not vars(results):
    parser.print_help()
    parser.exit(1)
