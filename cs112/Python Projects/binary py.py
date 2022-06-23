def make_bitseq(s: str) -> str:
	if not s.isascii():
		raise ValueError("Ascii only")
	return " ".join(f"{ord(i):08b}" for i in s)

