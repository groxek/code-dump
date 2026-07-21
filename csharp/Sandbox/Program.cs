using System.Text;

namespace Sandbox;

public static class Program
{
    public static void Main()
    {
        int startBalance = int.MaxValue;
        int sumTransaction = 500_000;
        int newBalance = startBalance + sumTransaction;

        System.Console.WriteLine(newBalance);
        System.Console.WriteLine($"0x{newBalance.ToString("X")}");
        System.Console.WriteLine($"{0:# ### ### ###}newBalance");
        
        string tableName = "name";
        string targetColumn = "yo";
        int limitValue = 4;

        StringBuilder result = new StringBuilder();
        result.Append($"SELECT {targetColumn} FROM {tableName} LIMIT {limitValue}");
        result.Replace($"{tableName}", "newname");
        System.Console.WriteLine(result);
    }
}