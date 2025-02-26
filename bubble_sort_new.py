from __future__ import annotations


def find_common_tags(articles: list[dict[str, list[str]]]) -> set[str]:
    if not articles:
        return set()

    # Start with the tags from the first article converted to a set
    common_tags = set(articles[0]["tags"])

    # Intersect with the tags from the subsequent articles
    for article in articles[1:]:
        common_tags.intersection_update(article["tags"])

        # If common tags become empty, there is no need to continue
        if not common_tags:
            return set()

    return common_tags
