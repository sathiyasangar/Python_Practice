def incrementor():
    info = {"count": 0}
    def number():
        info["count"] += 1
        return info["count"]
    return number

number = incrementor()
