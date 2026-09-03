class EdgeCaseUnitTestCoverageSynthesizerClient:
    def synthesize_edge_case_tests(self, source_function_code='def calculate_discount(price, pct): return price * (1 - pct / 100)', target_framework='pytest'):
        return {
            'test_suite_id': 'tst_syn_8812',
            'target_framework': target_framework,
            'generated_test_cases_count': 6,
            'covered_edge_conditions': ['Zero price', 'Negative discount percentage', '100% discount full waiver', 'Floating point precision rounding'],
            'synthesized_test_code': 'def test_calculate_discount_zero(): assert calculate_discount(0, 20) == 0\ndef test_calculate_discount_100(): assert calculate_discount(50, 100) == 0',
            'projected_branch_coverage_pct': 100.0,
            'test_suite_artifact_url': 'https://tests.synthesizer.genpark.ai/suites/8812.py'
        }
