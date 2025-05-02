def strip_leading_zeros(n: str) -> str:
    return str(int(n)) if n != "0" else "0"

def is_valid_triplet(n: str) -> bool:
    return n.isdigit() and 1 <= len(n) <= 3

def validateIP(ip: str) -> bool:
    if not ip:
        return False
    parts = ip.strip().split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not is_valid_triplet(part):
            return False
        part = strip_leading_zeros(part)
        if not (0 <= int(part) <= 255):
            return False
    return True
