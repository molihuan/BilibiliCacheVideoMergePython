def fix_m4s(target_path: str, output_path: str, bufsize: int = 256 * 1024 * 1024) -> None:
    assert bufsize > 0
    with open(target_path, 'rb') as target_file:
        header = target_file.read(32)
        new_header = header.replace(b'000000000', b'')
        new_header = new_header.replace(b'$', b' ')
        new_header = new_header.replace(b'avc1', b'')
        with open(output_path, 'wb') as output_file:
            output_file.write(new_header)
            i = target_file.read(bufsize)
            while i:
                output_file.write(i)
                i = target_file.read(bufsize)


if __name__ == "__main__":
    fix_m4s("367013145_nb2-1-30280.m4s", "1.mp3")
