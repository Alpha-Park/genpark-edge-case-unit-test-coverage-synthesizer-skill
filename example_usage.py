from client import EdgeCaseUnitTestCoverageSynthesizerClient

def main():
    client = EdgeCaseUnitTestCoverageSynthesizerClient()
    res = client.synthesize_edge_case_tests('def divide(a, b): return a / b')
    print('Edge-Case Test Synthesizer: ' + res['test_suite_id'] + ' (Coverage: ' + str(res['projected_branch_coverage_pct']) + '%)')
    print('Cases Generated: ' + str(res['generated_test_cases_count']) + ' | Conditions: ' + ', '.join(res['covered_edge_conditions']))
    print('Suite URL: ' + res['test_suite_artifact_url'])

if __name__ == '__main__':
    main()
