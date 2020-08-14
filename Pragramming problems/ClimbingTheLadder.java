/*
Thus is a good problem. Any more efficient solution are most welcomed.

Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking.
The game uses Dense Ranking, so its leaderboard works like this:

- The player with the highest score is ranked number 1 on the leaderboard.
- Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    static int[] check_rank(int[] scores, int alice, int mn){
        
        int cur_rank = 1;
        //To optimise it, we will return the exsact next index of array of current score's rank.
        //Next time the iteration will occure till that point.
        
        int rt_data[] = new int[2];
        if(scores.length == 1){
            if(alice >= scores[0]){
                rt_data[1] = 1;
                rt_data[0] = 1;
                return rt_data;
            }
            else{
                rt_data[1] = 2;
                rt_data[0] = 2;
                return rt_data;
            }
        }
        else{
            for(int i=0; i<=mn; i++){

                if(scores[i] < alice){
                    rt_data[1] = cur_rank;
                    rt_data[0] = i;
                    return rt_data;
                }
                else if(scores[i] == scores[i+1]){

                    if(alice == scores[i]){
                        rt_data[1] = cur_rank;
                        rt_data[0] = i+1;
                        return rt_data;
                    }

                }
                else if(scores[i] > scores[i+1]){

                    cur_rank++;
                    if(scores[i] >= alice && scores[i+1] <= alice){

                        if(scores[i] == alice){
                            rt_data[1] = cur_rank-1;
                            rt_data[0] = i;
                            return rt_data;
                        }
                        else{
                            rt_data[1] = cur_rank;
                            rt_data[0] = i+1;
                            return rt_data;
                        }
                    
                    }

                }

            }
        }
        cur_rank = cur_rank+1;
        rt_data[1] = cur_rank;
        rt_data[0] = scores.length-2;
        return rt_data;

    }

    static int[] climbingLeaderboard(int[] scores, int[] alice) {

        int []ranks = new int[alice.length];
        int temp[] = new int[2];
        int mn = scores.length-2;

        for(int i=0;i<alice.length;i++){

            temp = check_rank(scores, alice[i], mn);
            mn = temp[0];
            System.out.println("rt_data: "+mn);
            ranks[i] = temp[1];

        }

        return ranks;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        
        int scores[] = {100, 100, 50, 40, 20, 10};
        int alice[] = {5, 25, 50, 120};
        
        int outputs[] = new int[alice.length];
        outputs = climbingLeaderboard(scores, alice);
        
        for(int i =0;i<outputs.length;i++){
            
            System.out.println(outputs[i]);
            
        }
        
    }
}
