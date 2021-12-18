from utils import read_all


def nibble_bits(hexstr):
    n = int(hexstr, 16)
    return [1 if n & (1 << (3-i)) else 0 for i in range(4)]


def as_bit_list(hexstr):
    return [bit for hex in list(hexstr) for bit in nibble_bits(hex)]


def get_type_id(bits):
    return bits[3:6]


def all_packets(bits):
    return __all_packets__(bits, [])


def __all_packets__(bits, acc):
    if all(map(lambda bit: bit == 0, bits)):
        return acc

    match get_type_id(bits):
        case [1, 0, 0]:
            packet, rest = get_literal_packet(bits)
            return __all_packets__(rest, acc + [packet])
        case _:
            packet, rest = get_operator_packet(bits)
            return __all_packets__(rest, acc + [packet])


def get_literal_packet(bits):
    [v1, v2, v3, _, _, _, *rest] = bits
    number, bits = get_literal_number_from_subpackets(rest)
    return ("literal", version_number(v1, v2, v3), number), bits


def get_operator_packet(bits):
    [v1, v2, v3, t1, t2, t3, length_type_id, *rest] = bits
    subpackets, bits = get_operator_subpackets(rest, length_type_id)
    return ("operator", version_number(v1, v2, v3), type_number(t1, t2, t3), subpackets), bits


def get_literal_number_from_subpackets(bits):
    number_bits = []

    while bits[0] == 1:
        chunk = bits[1:5]
        number_bits += chunk
        bits = bits[5:]

    # Take last chunk
    chunk = bits[1:5]
    number_bits += chunk
    bits = bits[5:]

    return bits_to_number(*number_bits), bits


def get_operator_subpackets(bits, length_type_id):
    match length_type_id:
        case 1:
            number_of_subpackets = bits_to_number(*bits[:11])
            subpackets = []
            bits = bits[11:]
            for _ in range(number_of_subpackets):
                subpacket, bits = get_packet(bits)
                subpackets += [subpacket]
            return subpackets, bits
        case _:
            subpackets_length = bits_to_number(*bits[:15])
            subpacket_bits = bits[15:subpackets_length+15]
            return all_packets(subpacket_bits), bits[subpackets_length+15:]


def get_packet(bits):
    match get_type_id(bits):
        case [1, 0, 0]:
            return get_literal_packet(bits)
        case _:
            return get_operator_packet(bits)


def version_number(v1, v2, v3):
    return bits_to_number(v1, v2, v3)


def type_number(t1, t2, t3):
    return bits_to_number(t1, t2, t3)


def bits_to_number(*bits):
    length = len(bits)
    result = 0
    for i, bit in enumerate(bits):
        result += bit << (length - 1) - i

    return result


def sum_version_numbers(packet):
    return __sum_version_numbers__([packet], 0)


def __sum_version_numbers__(packets, total):
    if packets == []:
        return total

    match packets[0]:
        case ("literal", version_number, _):
            return __sum_version_numbers__(packets[1:], total + version_number)
        case ("operator", version_number, _type, subpackets):
            return __sum_version_numbers__(packets[1:], total + version_number) + \
                __sum_version_numbers__(subpackets, 0)


def product(list):
    result = 1
    for item in list:
        result *= item
    return result


def evaluate_operator(packet):
    match packet:
        case ("operator", _v, 0, subs):
            return sum(map(evaluate_operator, subs))
        case ("operator", _v, 1, subs):
            return product(map(evaluate_operator, subs))
        case ("operator", _v, 2, subs):
            return min(map(evaluate_operator, subs))
        case ("operator", _v, 3, subs):
            return max(map(evaluate_operator, subs))
        case ("operator", _v, 5, [suba, subb]):
            return 1 if evaluate_operator(suba) > evaluate_operator(subb) else 0
        case ("operator", _v, 6, [suba, subb]):
            return 1 if evaluate_operator(suba) < evaluate_operator(subb) else 0
        case ("operator", _v, 7, [suba, subb]):
            return 1 if evaluate_operator(suba) == evaluate_operator(subb) else 0
        case ("literal", _v, n):
            return n
        case other:
            raise NotImplementedError(f"Other: {other}")


if __name__ == '__main__':
    input = read_all(16)

    [root_packet] = all_packets(as_bit_list(input.strip()))

    print(sum_version_numbers(root_packet))
    print(evaluate_operator(root_packet))
