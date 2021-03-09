from dataclasses import dataclass
from typing import Tuple


@dataclass
class Entry(object):
    ip_prefix: str
    ip_prefix_bin: str
    prefix_length: int
    as_number: str

    def is_match_and_output(self, ip_input) -> Tuple[bool, str]:
        does_match = False
        output_message = "There is no match"
        ip_input_bin = ''.join(map(lambda x: str(format(int(x), '08b')), ip_input.split(".")))

        if ip_input_bin[: self.prefix_length] == self.ip_prefix_bin:
            does_match = True
            output_message = f"{self.ip_prefix}/{self.prefix_length} {self.as_number} {ip_input}"

        return does_match, output_message


def is_valid_ip_add(ip) -> bool:
    ip_prefix_arr = ip.split(".")
    valid = True

    # not valid if not exactly 4 numbers
    if len(ip_prefix_arr) != 4:
        valid = False
    # not valid if any entry is empty
    elif sum(i.strip() == "" for i in ip_prefix_arr) > 0:
        valid = False
    # not valid if any entry is greater than 255
    elif sum(int(i) > 255 for i in ip_prefix_arr) > 0:
        valid = False

    return valid















