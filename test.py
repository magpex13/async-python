import asyncio
import unittest
from main import randon_numbers

class TestRandomNumbers(unittest.TestCase):
    def test_one_random_number(self):
        return self.assertEqual(len(asyncio.run(randon_numbers(1))),1)
    def test_two_random_number(self):
        return self.assertTrue(len(asyncio.run(randon_numbers(2))) == 2)
    def test_three_random_number(self):
        return self.assertTrue(len(asyncio.run(randon_numbers(3))) == 3)
    
async def test_one_random_number():
    return await randon_numbers(1)
async def test_two_random_number():
    return await randon_numbers(2)
async def test_three_random_number():
    return await randon_numbers(3)

if __name__ == "__main__":
    rn_one = asyncio.run(test_one_random_number())
    rn_two = asyncio.run(test_two_random_number())
    rn_three = asyncio.run(test_three_random_number())
    assert len(rn_one) == 1
    assert len(rn_two) == 2
    assert len(rn_three) == 3
    print("Everything ok!")

    unittest.main()