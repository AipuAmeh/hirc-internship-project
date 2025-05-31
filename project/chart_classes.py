class Charts:
    def __init__(self):
        pass

    def bar_chart_query(self):
        query = """
        SELECT PM_NAME_1 AS project_manager, RSCH_CATG as research_category, COUNT(DISTINCT RSCH_CATG) as count
        FROM data
        WHERE PM_NAME_1 IS NOT NULL
        GROUP BY PM_NAME_1
        ;
    """
        return query