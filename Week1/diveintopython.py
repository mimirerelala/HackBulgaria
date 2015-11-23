from firstday import to_digits, palindrome, char_histogram

# 1.Is Number Balanced?


def is_number_balanced(n):
    number = to_digits(n)
    if n >= 0 and n < 10:
        return True
    number_len = len(number)
    if (number_len % 2 == 0):
        const = 0
    else:
        const = 1
    left = sum(number[0:number_len//2])
    right = sum(number[(number_len//2+const):])
    if left == right:
        return True
    else:
        return False

print(is_number_balanced(9))
print(is_number_balanced(4518))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))


# 2. Increasing and Decreasing Sequencies
# 2.1 Increasing

def is_increasing(seq):
    for i in range(1, len(seq)):
        if seq[i] <= seq[i-1]:
            return False
    return True

print(is_increasing([1, 2, 3, 4, 5]))
print(is_increasing([1]))
print(is_increasing([5, 6, -10]))
print(is_increasing([1, 1, 1, 1]))

# 2.2 Decreasing sequence


def is_decreasing(seq):
    for i in range(1, len(seq)):
        if seq[i] >= seq[i-1]:
            return False
    return True

print(is_decreasing([5, 4, 3, 2, 1]))
print(is_decreasing([1, 2, 3]))
print(is_decreasing([100, 50, 20]))
print(is_decreasing([1, 1, 1, 1]))

# 3. Largest Palindrome


def get_largest_palindrome(n):
    for i in range(n-1, 0, -1):
        if palindrome(i):
            return i

print(get_largest_palindrome(99))
print(get_largest_palindrome(252))
print(get_largest_palindrome(994687))
print(get_largest_palindrome(754649))

# Prime Numbers


def prime_numbers(n):
    all_numbers = set(range(2, n+1))
    for i in range(2, n):
        current_num = i+i
        while current_num <= n:
            all_numbers.discard(current_num)
            current_num += i
    return list(all_numbers)

print(prime_numbers(100))
print(prime_numbers(30))
print(prime_numbers(3))

# 5. Anagrams


def is_anagram(a, b):
    a = a.lower()
    b = b.lower()
    hist_a = char_histogram(a)
    hist_b = char_histogram(b)

    for key in hist_a:
        if hist_a[key] != hist_b[key]:
            return False
    return True

print(is_anagram("BRADE", "BeaRD"))
print(is_anagram("TOP_CODER", "COTO_PRODE"))

# b6 Birthday Range


def birthday_ranges(birthdays, ranges):
    result = []
    for current_range in ranges:
        curret_sum = 0
        (start, end) = cu
        rrent_range
        for i in range(len(birthdays)):
            if birthdays[i] >= start and birthdays[i] <= end:
                curret_sum += 1
        result.append(curret_sum)
    return result

print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))


# 7. Sum Numbers in Matrix

def sum_matrix(m):
    sum = 0
    for row in m:
        for col in row:
            sum += col
    return sum


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m))
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(sum_matrix(m))
m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sum_matrix(m))


# 8. Matrix Bombing

def calculate_sum(m, i, j):
    rows = len(m)
    cols = len(m[0])
    sum = 0
    current_position_points = m[i][j]
    for l in range(i-1, i+2, 1):
        for k in range(j-1, j + 2, 1):
            if l >= 0 and l < rows and k >= 0 and k < cols:
                if not (l == i and k == j):
                    value_to_add = m[l][k] - current_position_points
                    if value_to_add < 0:
                        sum += m[l][k]
                    else:
                        sum += current_position_points

    return sum


def matrix_bombing_plan(m):
    rows = len(m)
    cols = len(m[0])
    result = {}
    for row in range(rows):
        for col in range(cols):
            tuple_key = (row, col)
            result[tuple_key] = sum_matrix(m) - calculate_sum(m, row, col)

    return result

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix_bombing_plan(m))

# 9.1 Is Transversal


def is_transversal(transversal, family):
    if len(family) != len(transversal):
        return False
    for tuple_key in family:
        for j in range(len(tuple_key)):
            if tuple_key[j] in transversal:
                family = tuple(x for x in family if x != tuple_key)
                transversal = tuple(x for x in transversal if x != tuple_key[j])
                break
    if len(family) > 0:
        return False
    return True

print(is_transversal((4, 5, 6), ((5, 7, 9), (1, 4, 3), (2, 6))))
print(is_transversal((1, 2), ((1, 5), (2, 3), (4, 7))))
print(is_transversal((2, 3, 4), ((1, 7), (2, 3, 5), (4, 8))))

# 9.2 All transversals


def generate_transversals(family):
    list_all = []
    m = len(family)
    for i in range(m):
        for k in range(len(family[m])):
            small_list = 0
            small_list.append(family[m][k])


print(generate_transversals([[1, 4, 5], [2, 7], [1, 9]]))
print(generate_transversals([[7, 8], [2, 3, 4]]))
