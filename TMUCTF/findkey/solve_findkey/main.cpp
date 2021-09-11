/*
	author: gnudnaod
	create: ..............
*/

#include <bits/stdc++.h>
#define F(i,a,b) for (int i = a; i <= b; i++)
#define _F(i,a,b) for (int i = a; i >= b; i--)
#define ll long long
#define pb push_back

using namespace std;

const int maxn = 100;

int n;
char key[30];

int final_check(int a1, int a2, int a3)
{
  int result; // eax@4

  if ( 4 * a1 + 2 * a2 != -966590128 || 2 * a2 + a3 != -467021804 || a2 != 1163735118 )
    result = puts("Sorry! Try Harder...");
  else
    result = printf("Well Done! TMUCTF{%s}\n", key);
  return result;
}

int first_check(int a1, int a2, int a3)
{
  int result; // eax@2

  if ( a2 == -706026796 )
    result = final_check(a1 - 176506699, 2 * a3 + 2 * a1, a1);
  else
    result = puts("Sorry! Try Harder...");
  return result;
}

int main()
{
  int v3; // edx@6
  unsigned int v5; // [sp+0h] [bp-90h]@7
  int v6; // [sp+4h] [bp-8Ch]@9
  int v7; // [sp+8h] [bp-88h]@10
  int v8; // [sp+Ch] [bp-84h]@10
  int v9[26]; // [sp+10h] [bp-80h]@4
  int v10; // [sp+78h] [bp-18h]@6
  int v11; // [sp+7Ch] [bp-14h]@6
  int v12; // [sp+80h] [bp-10h]@6
  int v13; // [sp+84h] [bp-Ch]@1
  int j; // [sp+88h] [bp-8h]@6
  int i; // [sp+8Ch] [bp-4h]@3

  printf("Please enter the key: ");//, argv, envp);
  scanf("%s", key);
  v13 = strlen(key);
  if ( v13 == 16 )
  {
    for ( i = 0; i < v13 / 4; ++i )
      v9[i + 4] = (((((key[4 * i + 3] << 8) + key[4 * i + 2]) << 8) + key[4 * i + 1]) << 8) + key[4 * i];
    v12 = (((v9[4] >> 3) & 0x20000000) + 32 * v9[4]) ^ v9[4];
    v11 = v12 ^ (v12 << 7);
    v10 = (unsigned __int8)((v12 ^ (v12 << 7)) >> 1) + (v12 ^ (v12 << 7));
    v9[25] = v10 ^ (((v10 >> 3) & 0x20000000) + 32 * v10);
    v9[24] = (((v9[5] >> 3) & 0x20000000) + 32 * v9[5]) ^ v9[5];
    v9[23] = v9[24] ^ (v9[24] << 7);
    v9[22] = (unsigned __int8)((v9[24] ^ (v9[24] << 7)) >> 1) + (v9[24] ^ (v9[24] << 7));
    v9[21] = v9[22] ^ (((v9[22] >> 3) & 0x20000000) + 32 * v9[22]);
    v9[20] = (((v9[6] >> 3) & 0x20000000) + 32 * v9[6]) ^ v9[6];
    v9[19] = v9[20] ^ (v9[20] << 7);
    v9[18] = (unsigned __int8)((v9[20] ^ (v9[20] << 7)) >> 1) + (v9[20] ^ (v9[20] << 7));
    v9[17] = v9[18] ^ (((v9[18] >> 3) & 0x20000000) + 32 * v9[18]);
    v9[16] = (((v9[7] >> 3) & 0x20000000) + 32 * v9[7]) ^ v9[7];
    v9[15] = v9[16] ^ (v9[16] << 7);
    v9[14] = (unsigned __int8)((v9[16] ^ (v9[16] << 7)) >> 1) + (v9[16] ^ (v9[16] << 7));
    v3 = (v9[14] >> 3) & 0x20000000;
    v9[13] = v9[14] ^ (v3 + 32 * v9[14]);
    for ( j = 0; j < v13 / 4; ++j )
    {
      v9[12] = v9[j] ^ (v9[j] << 7);
      v9[11] = (unsigned __int8)(v9[12] >> 1) + v9[12];
      *(&v5 + j) = v9[11];
    }
    if ( v6 == -231060518 )
      first_check(v5, v7, v8);
    else
      puts("Sorry! Try Harder...");
    }
    else
    {
      puts("Sorry! Try Harder...");
    }
  return 0;
}
