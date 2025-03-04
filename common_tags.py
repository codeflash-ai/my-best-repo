from __future__ import annotations


def find_common_tags(articles: list[dict[str, list[str]]]) -> set[str]:
    if not articles:
        return set()

    # Initialize the common_tags set from the first article's tags
    common_tags = set(articles[0]["tags"])

    # Use set intersection to find common tags with all other articles' tags
    for article in articles[1:]:
        common_tags.intersection_update(article["tags"])

    return common_tags
