from planner import plan_and_execute

if __name__ == "__main__":
    user_goal = "Find next SpaceX launch, check weather there, and see if it may be delayed."
    result = plan_and_execute(user_goal)
    print(result)
