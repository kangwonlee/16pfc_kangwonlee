# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex39.html


def new(num_buckets=256):
    """
    Initializes a Map with the given number of buckets.
    :param num_buckets:
    :return:
    """
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap


def hash_key(aMap, key):
    """
    Given a key this will create a number and then convert it to an index for the aMap's buckets.
    :param aMap:
    :param key:
    :return:
    """
    return hash(key) % len(aMap)


def get_bucket(aMap, key):
    """
    Given a key, find the bucket where it would go.
    :param aMap:
    :param key:
    :return:
    """
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]


def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key and default (None if not set) when not found.
    :param aMap:
    :param key:
    :param default:
    :return:
    """
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v

    return -1, key, default


# 여기까지 입력 후 add, commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit  # 오류노트 에 각자 오류노트 작성
