import random

from generators.generator import Generator


class BirthdateGenerator(Generator):
    def generate(self):
        # 생년월일 생성 로직 구현
        year = random.randint(1970, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"
