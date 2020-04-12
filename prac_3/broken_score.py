def main():


    def check_position(score):
        """Check position according to the given score."""
        if score < 0 or score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"

    """Get score and show the position."""
    score = float(input("Please Enter the score: "))
    print(check_position(score))


main()
