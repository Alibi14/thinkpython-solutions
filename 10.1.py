def nested_sum(nestedList):
        new_list = []

        def flatlist(nestedList):
                for i in range(len(nestedList)):
                        if type(nestedList[i]) == int:
                                new_list.append(nestedList[i])
                        else:
                                flatlist(nestedList[i])
                return new_list
        flatlist(nestedList)
        print(sum(new_list))


nested_sum([[1, 2, 3], [4,5,6]])






