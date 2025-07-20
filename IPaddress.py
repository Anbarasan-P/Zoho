def restore_ip_addresses(s):
    result = []

    def backtrack(start, path):
        # If we have 4 parts and reached end of string, it's valid
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return

        # Try parts of length 1 to 3
        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start+length]

            # Check for leading zeros and value range
            if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                continue

            backtrack(start + length, path + [segment])

    backtrack(0, [])
    return result


print(restore_ip_addresses("25525511135"))
# Output: ['255.255.11.135', '255.255.111.35']

print(restore_ip_addresses("0000"))
# Output: ['0.0.0.0']

print(restore_ip_addresses("101023"))
# Output: ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']

