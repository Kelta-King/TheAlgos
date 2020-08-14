/*

HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly 5 people on social media.

On the first day, half of those  people (i.e., floor(5/2) ) like the advertisement and each shares it with 3 of their friends.
At the beginning of the second day,  people receive the advertisement.
Each day, floor(recipient/2) of the recipients like the advertisement and will share it with 3 friends on the following day. 
Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.

*/

using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution {

    // Below method is beig used to determine the number of recipients likes the ad.
    
    static int viralAdvertising(int n) {

        int recipients = 5;
        int temp = 0;
        int likes = 0;

        for(int i=1; i<=n; i++){

            temp = recipients/2;
            likes += temp;
            recipients = temp*3;

        }

        return likes;

    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int result = viralAdvertising(n);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
