import sentry_sdk

SENTRY_LIKE_DSN = 'http://e6db5288ee8141e6ba4e07b056a5de5c@0.0.0.0:8000/1'

if __name__ == '__main__':
    sentry_sdk.init(SENTRY_LIKE_DSN)

    division_by_zero = 1 / 0

