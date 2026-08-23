class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            operation = operations[i]
            try:
                operationInt = int(operation)
                record.append(operationInt)
            except ValueError:
                match operation:    
                    case "+":
                        record.append(record[len(record)-1] + record[len(record)-2])
                    case "D":
                        record.append(2 * record[len(record)-1])
                    case "C":
                        record.pop()

        return sum(record)
            
            