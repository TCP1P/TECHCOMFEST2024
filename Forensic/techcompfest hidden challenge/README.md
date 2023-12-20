# techcompfest hidden challenge

## description

I found this hidden challenge in techcompfest website. But this challenge is not listed in the challenge list. And there is an limited time to download the file. So I download it immediately while capturing the traffic using wireshark so i can review it later. Please i need you to help me to solve this challenge. I'm not good at **pwning** but I can fix the file given to get that binary. Here is the pcap file. I think the website still up but we can't download it anymore, but you can find it in my captured traffic. I hope you can help me to solve this challenge. Thank you.

## how to solve

1. open the pcap file using wireshark
2. follow the tcp stream of http traffic
3. find download file
4. save the file
5. fix the zip file to get binary file
6. connect to the server using netcat and pwn it

## flag

TCF2024{foren_pwn?_pengen_turu_aja_lah_capek_challnya_gajelas}