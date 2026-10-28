"""Tests for PageIndex page-range post-processing."""

import unittest

from vendor.pageindex.pageindex.utils import post_processing


class PostProcessingTests(unittest.TestCase):
    def test_same_page_next_section_does_not_reverse_range(self):
        structure = [
            {
                "structure": "1",
                "title": "PLANNING",
                "physical_index": 12,
                "appear_start": "no",
            },
            {
                "structure": "2",
                "title": "PRODUCT REALIZATION",
                "physical_index": 12,
                "appear_start": "yes",
            },
        ]

        result = post_processing(structure, end_physical_index=12)

        self.assertEqual(result[0]["start_index"], 12)
        self.assertEqual(result[0]["end_index"], 12)

    def test_later_page_start_still_ends_previous_page(self):
        structure = [
            {
                "structure": "1",
                "title": "PLANNING",
                "physical_index": 12,
                "appear_start": "no",
            },
            {
                "structure": "2",
                "title": "PRODUCT REALIZATION",
                "physical_index": 13,
                "appear_start": "yes",
            },
        ]

        result = post_processing(structure, end_physical_index=13)

        self.assertEqual(result[0]["start_index"], 12)
        self.assertEqual(result[0]["end_index"], 12)


if __name__ == "__main__":
    unittest.main()
