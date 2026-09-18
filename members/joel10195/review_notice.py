def review_notice(score):
    if score >= 80:
        return "리뷰를 통과했습니다."
    return "수정이 필요합니다..."


print(review_notice(90))
print(review_notice(60))
