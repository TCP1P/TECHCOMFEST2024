# kuli-ah forensics (easy)

## description

I just created secret message in image file but i want to make it secure so i transform it to audio file. But i think it's not secure enough so i archive it with password. I encrypt it with very strong password. I'am sure no one can crack it because my password is random 15 digit number in base 3. It's very very secure right? ... right??. Then i wrap my file within an image so no one can realize.

flag = TCF2024{`<my secret message>`}

## how to solve

1. It mentioned that the password is 15 character number in base 3. So we can bruteforce it using john or maybe python script.
2. It will take several time to bruteforce, mine is arround 2 - 3 minutes. `john --mask=[0-2][0-2][0-2][0-2][0-2][0-2][0-2][0-2][0-2][0-2][0-2][0-2][0-2][0-2][0-2] hash`
3. After we get the password `012012010121022`, we can extract the archive and get the audio.
4. Then we can use sstv decoder to view the image.

## flag

TCF2024{w0w_congrats_you_win}