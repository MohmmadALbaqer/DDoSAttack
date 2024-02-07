from colorama import Fore, Style
import os 
os.system("clear")

art = r"""
			       /T /I
                              / |/ | .-~/
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l   |  T  /
     T\ |  \ Y l  /T   | \I  l   \ `  l Y
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  /    ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]
^.___~"--._    ~-{  .-~ .  `\ Y . /    |
 <__ ~" -.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.
              (_/ .  ~(   /'     "~ "--,Y   -=b-. _)
               (_/ .  \  :           / l      c"~o \
                \ /    `.    .     .^   \_.-~"~--.  )
                 (_/ .   `  /     /       !        )/
                  / / _.   '.   .':      /        '
                  ~(_/ .   /    _  `  .-<_
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K    "-.~-.______//
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                       /' /\     \  \     ,v=.  ((        ·▄▄▄▄  ·▄▄▄▄        .▄▄ ·
                    .^. / /\      "  }__ //===-  `        ██· ██ ██· ██  ▄█▀▄ ▐█ ▀. 
                   / / ' '  "-.,__ {---(==-               ▐█▪ ▐█▌▐█▪ ▐█▌▐█▌.▐▌▄▀▀▀█▄
                 .^ '       :  T  ~"   ll                 ██. ██ ██. ██ ▐█▌.▐▌▐█▄▪▐█
                 / .  .  . : | :!        \\               ▀▀▀▀▀• ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ 
               (_/  /   | | j-"           ~^       
                 ~-<_(_.^-~"
                        
                                        
                                             ▄▄▄· ▄▄▄▄▄▄▄▄▄▄ ▄▄▄·  ▄▄· ▄ •▄ ▪   ▐ ▄  ▄▄ • 
                                            ▐█ ▀█ •██  •██  ▐█ ▀█ ▐█ ▌▪█▌▄▌▪██ •█▌▐█▐█ ▀ ▪
                                            ▄█▀▀█  ▐█.▪ ▐█.▪▄█▀▀█ ██ ▄▄▐▀▀▄·▐█·▐█▐▐▌▄█ ▀█▄
                                            ▐█▪ ▐▌ ▐█▌· ▐█▌·▐█▪ ▐▌▐███▌▐█.█▌▐█▌██▐█▌▐█▄▪▐█
                                             ▀  ▀  ▀▀▀  ▀▀▀  ▀  ▀ ·▀▀▀ ·▀  ▀▀▀▀▀▀ █▪·▀▀▀▀ 

"""

colored_art = f"{Fore.YELLOW}{art}{Style.RESET_ALL}"

print(colored_art)

def main():
    print(f"{Fore.BLUE}[{Fore.RED}1{Fore.BLUE}] - {Fore.GREEN}Arabic{Style.RESET_ALL} ")
    print(f"{Fore.BLUE}[{Fore.RED}2{Fore.BLUE}] - {Fore.GREEN}English")

    choice = input("[+] About (1 - 2): ")

    if choice == "1":
        print("لقد اخترت اللغة العربية.")
        print('''أداة DDoS (هجوم خدمة الإنكشاف) تُستخدم لتنفيذ هجمات DDoS، وهي عبارة عن هجمات تهدف إلى إعاقة خدمة الإنترنت للمستخدمين النهائيين عن طريق زيادة حجم حركة المرور أو استنزاف الموارد المتاحة. هناك العديد من الأدوات المخصصة لتنفيذ هجمات DDoS، ولكن يجب التأكيد على أن استخدامها بدون إذن قانوني يعد غير قانوني وغير أخلاقي.

تتنوع أدوات DDoS في مستويات التعقيد والفعالية، ويمكن أن تشمل بعضها الأدوات المفتوحة المصدر والأخرى الخاصة. بعض الأدوات الشهيرة المستخدمة لهجمات DDoS .

يرجى العلم بأن استخدام هذه الأدوات بشكل غير قانوني أمر محظور ويعتبر جريمة. هجمات DDoS تعتبر انتهاكًا للقوانين الرقمية في العديد من الدول، وقد يتسبب استخدامها في عواقب قانونية خطيرة. يجب أن يتم استخدام هذه الأدوات فقط لأغراض اختبار الأمان بشكل قانوني وبموافقة صاحب النظام المستهدف.''')

    elif choice == "2":
        print("You chose English language.")
        print('''DDoS tool is used to carry out DDoS attacks, which are attacks that aim to disrupt Internet service for end-users by increasing traffic volume or depleting available resources. There are many tools dedicated to carrying out DDoS attacks, but it must be emphasized that using them without legal permission is illegal and unethical.

DDoS tools vary in complexity and effectiveness, and some can include both open source and proprietary tools. Some of the famous tools used for DDoS attacks.

Please be aware that using these tools illegally is prohibited and considered a crime. DDoS attacks are a violation of digital laws in many countries, and their use can cause serious legal consequences. These tools should only be used for security testing purposes legally and with the consent of the owner of the target system.''')

if __name__ == "__main__":
    main()
