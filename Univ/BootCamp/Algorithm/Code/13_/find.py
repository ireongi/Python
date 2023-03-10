from operator import itemgetter


## 함수 선언 부분 ##
def make_index(array, position):
    before_array = []
    index = 0
    for idx in array(len(array)):
        before_array.append((idx[position], index))
        index += 1

    sorted_array = sorted(before_array, key=itemgetter(0))
    return sorted_array


def book_search(array, fData):
    pos = -1
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if fData == array[mid][0]:
            return array[mid][1]
        elif fData > array[mid][0]:
            start = mid + 1
        else:
            end = mid - 1

    return pos


## 전역 변수 선언 부분 ##
book_array = [['어린왕자', '쌩떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'],
              ['신곡', '단테'], ['돈키호테', '세르반테스'], ['동물농장', '조지오웰'],
              ['데미안', '헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅']]
name_index = []
auth_index = []


## 메인 코드 부분 ##
print('#책장의 도서 ==>', book_array)
name_index = make_index(book_array, 0)
print('#도서명 색인표 ==>', name_index)
auth_index = make_index(book_array, 1)
print('#작가명 색인표 ==>', auth_index)

find_name = '신곡'
find_pos = book_search(name_index, find_name)
if find_pos != -1:
    print(f"{find_name}의 작가는 {book_array[find_pos][1]}입니다.")
else:
    print(f"{find_name} 책은 없습니다.")

find_name = '괴테'
find_pos = book_search(auth_index, find_name)
if find_pos != -1:
    print(f"{find_name}의 도서는 {book_array[find_pos][0]}입니다.")
else:
    print(find_name, ' 작가는 없습니다.')
