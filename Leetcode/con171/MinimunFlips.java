class Solution {
    public int minFlips(int a, int b, int c) {
        int count = 0;
        int az, bz, cz;
        while (!(a == 0 && b == 0 && c == 0)){
            az = a % 2;
            bz = b % 2;
            cz = c % 2;
            if ( (az | bz) != cz){
                if ( cz == 0){
                    count = count + az + bz;
                } else{
                    count += 1;
                }

            }

            a /= 2;
            b /= 2;
            c /= 2;
        }
        
       return count;
    }
}