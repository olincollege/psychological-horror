import pygame
import pytest
import constants
import utils


def test_new_event():
    """
    Tests whether the new_event function returns unique events
    """
    nums = set()
    runs = 10
    for _ in range(runs):
        nums.add(utils.new_event())
    assert len(nums) == runs


def test_animation_info():
    """
    Tests whether the get_animation_info returns the stuff from /test_animations
    """
    pygame.init()
    screen = pygame.display.set_mode((1, 1))
    info = utils.get_animation_info("test_animations")
    assert len(info['animations']) == 4
    assert info['positions'] == [(1, 2), (3, 4), (5, 6), (7, 8)]
    assert info['frame_length'] == constants.FRAME_RATE / 5


IS_SWORD_CASES = [
    ((0, 0, 0), False),
    ((255, 255, 255), False),
    ((255, 0, 0), False),
    ((0, 255, 0), False),
    ((0, 0, 255), False),
    ((255, 255, 0), False),
    ((255, 0, 255), False),
    ((0, 255, 255), False),
    ((150, 150, 150), True),
    ((150, 151, 152), True),
    ((110, 200, 120), False),
]


@pytest.mark.parametrize("color,is_sword", IS_SWORD_CASES)
def test_is_sword(color, is_sword):
    """
    Tests whether the is_sword function properly detects swords
    """
    assert utils.is_sword(color) == is_sword
