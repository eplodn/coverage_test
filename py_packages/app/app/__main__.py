import signal
import os
import sys

from flask import Flask, jsonify
from flask_restful import Api

from infra import utils

if os.environ.get('COLLECT_COVERAGE') == '1':
    print("WILL COLLECT COVERAGE")
    import coverage
    coverage_dir = '/coverage/'
    if not os.path.exists(coverage_dir):
        os.makedirs(coverage_dir)

    cov = coverage.Coverage(data_file=f'{coverage_dir}/.coverage',
                            data_suffix=True,
                            include=['*/app/*', '*/infra/*'])
    cov.start()
else:
    cov = None
    print("WILL *NOT* COLLECT COVERAGE")


def clean_exit():
    if cov:
        cov.stop()
        cov.save()


def clean_sigterm(*args, **kwargs):
    print("INSIDE clean_sigterm")
    try:
        clean_exit()
        signal.signal(signal.SIGTERM, original_sigterm_cb)
        os.kill(os.getpid(), signal.SIGTERM)
    except Exception:
        os._exit(1)


def clean_sigint(*args, **kwargs):
    print("INSIDE clean_sigint")
    try:
        clean_exit()
        signal.signal(signal.SIGINT, original_sigint_cb)
        os.kill(os.getpid(), signal.SIGINT)
    except Exception:
        os._exit(1)


app = Flask('eplodn_flask_app')
api = Api(app)


original_sigterm_cb = signal.getsignal(signal.SIGTERM)
original_sigint_cb = signal.getsignal(signal.SIGINT)


def main():
    signal.signal(signal.SIGTERM, clean_sigterm)
    signal.signal(signal.SIGINT, clean_sigint)

    app.run(host='0.0.0.0', port=5005, debug=True, threaded=True)


@app.route('/<string:somenumber>', methods=('GET', 'POST'))
def check_number(somenumber):
    int_number = int(somenumber)
    result = utils.check(int_number)
    return jsonify({'status': 'alive', 'number': somenumber, 'result': result})


if __name__ == '__main__':
    sys.exit(main())

