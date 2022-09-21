from typing import List, Optional, Dict, Callable

import functions

FILE_NAME: str = "data/apache_logs.txt"

CMD_TO_FUNCTIONS: Dict[str, Callable] = {
    "filter": functions.filter_query,
    "map": functions.map_query,
    "unique": functions.unique_query,
    "sort": functions.sort_query,
    "limit": functions.limit_query,
    "regex": functions.regex_query
}


def build_query(cmd: str, param: str, data: Optional[List[str]]) -> List[str]:
    if data is None:
        with open(FILE_NAME) as file:
            prepared_data: List[str] = list(map(lambda x: x.strip(), file))
    else:
        prepared_data = data

    return CMD_TO_FUNCTIONS[cmd](param=param, data=prepared_data)
