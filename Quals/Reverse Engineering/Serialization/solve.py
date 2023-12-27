def decode_serial(serial_number):
    tokens = serial_number.split("-")
    
    size = int(len(tokens) ** 0.5)
    matrix = [[0] * size for _ in range(size)]
    sbox = [[0] * size for _ in range(size)]
    
    row = 0
    col = 0
    
    for token in tokens:
        matrix[row][col] = int(token[4:], 16)
        sbox[row][col] = (int(token[0:2], 16), int(token[2:4], 16))
        
        col += 1
        if col == size:
            row += 1
            col = 0
            
    return matrix, sbox

def decode_spiral(matrix):
    if not matrix:
        return []

    result = []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom and left <= right:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

serial_number = "04000218-01000360-05030548-01050358-070202f8-03040548-020001a0-040102f8-04020548-01070298-04040548-06000370-060502f8-030503a0-07000188-070602f8-02060398-04030548-000601a0-00050190-050002f8-06020268-07030280-02010228-03020548-03010290-040703b0-03000340-060101a0-00020230-03070360-07040280-000703d8-01010360-07010210-060302f8-030602f8-07050218-00030190-050403e8-010401a0-00040180-040602c8-01030268-05010220-04050328-060603a8-02030268-02020168-02070180-060401a0-05020548-06070370-00010218-01060198-010202f8-02040308-05050390-000002a0-07070338-05060180-03030548-02050398-05070188"
matrix, sbox = decode_serial(serial_number)

new_matrix = [[0] * len(matrix) for _ in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        new_matrix[sbox[i][j][0]][sbox[i][j][1]] = matrix[i][j]//8

flag = ''
for c in decode_spiral(new_matrix):
    flag += chr(c)

print(flag)