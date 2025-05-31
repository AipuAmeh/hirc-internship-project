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
    
    def pie_chart_query(self):
        query = """
        SELECT RSCH_TYPE AS research_type, COUNT(RSCH_TYPE) AS count
        FROM data
        WHERE RSCH_TYPE IS NOT NULL
        GROUP BY RSCH_TYPE
        ;
        """
        return query