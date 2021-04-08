from .models import *

def declare_chal(data):
    chal = Challenges.query.filter_by(name=data["name"]).first()
    if chal is not None:
        for n in data:
            if n == "name": continue
            setattr(chal, n, data[n])
    else:
        data["solves"] = "0"
        db.session.add(Challenges(**data))
    db.session.commit()

# PokeCTF 2021
def create_update_chals():
    declare_chal({ "name": "Sanity check",
        "category": "misc",
        "score": 25,
        "info": """

    Look in the description of the announcement channel in the discord server for it!

    """,
    "flag": 'poke{k33p_y0ur_s4nity!}'
    })

    declare_chal({ "name": "Deadbeef",
        "category": "pwn",
        "score": 50,
        "info": """

    Warm-up challenge!

    Files (Source and Binary): <a href="/static/deadbeef.zip">deadbeef.zip</a>

    Connect with: nc matrx.me 5001

    """,
    "flag": 'poke{sh0uld_h4ve_writt3n_it_1n_rust}'
    })

    declare_chal({ "name": "Printer",
        "category": "pwn",
        "score": 200,
        "info": """

    I set up this printer service last week.
    Do not forget to specify the format!

    Files (Source and Binary): <a href="/static/printer.zip">printer.zip</a>

    Connect with: nc matrx.me 5002

    """,
    "flag": 'poke{s0_th4t\'s_why_th3y_alw4ys_br34k}'
    })


    declare_chal({ "name": "Simple Instructions",
        "category": "reverse",
        "score": 50,
        "info": """
    Binary: <a href="/static/simple_instructions.zip">simple_instructions.zip</a>

    You shouldn't have trouble with this one...
    """,
        "flag": 'poke{s1mpl3_instructi0ns_r1ght?}'
    })


    declare_chal({ "name": "Slow and steady",
        "category": "reverse",
        "score": 100,
        "info": """
    Binary: <a href="/static/slow_and_steady.zip">slow_and_steady.zip</a>

    This flag-printing binary I just made is a bit slow.
    I wonder if you can optimize my code a bit?

    """,
        "flag": 'poke{sl0w_4nd_st3ady_w1ns_the_r4ce}'
    })

    declare_chal({ "name": "newborn vm",
        "category": "reverse",
        "score": 50,
        "info": """
    Please help me find a pacifier, I cannot endure these screams any longer.
    Here, take it <a href="/static/vm_reverse/newborn_vm.zip">newborn_vm.zip</a> and hopefully I won't hear any more "poke..." screams.

    <b>Note:</b> All four vm challenges use the same binary baby_vm.
    The only thing that changes is the code run by the vm.
    With each stage, you should probably reverse more and more of the binary.
    You only need to reverse a small portion (or maybe nothing at all ;) for the first stage.

    """, # TODO
        "flag": 'poke{n0_r3ving_n3cess4ry}'
    })

    declare_chal({ "name": "baby vm",
        "category": "reverse",
        "score": 100,
        "info": """
    Finally, some peace and quiet.
    Maybe a bit too quiet.
    Can you try and get them to say their first word?: <a href="/static/vm_reverse/baby_vm.zip">baby_vm.zip</a>!

    """, # TODO
        "flag": 'poke{n0_jump1ng_n3cessary}'
    })

    declare_chal({ "name": "kid vm",
        "category": "reverse",
        "score": 200,
        "info": """
    Barely able to walk and they just won't stop jumping around all over the place!
    Please help me calm them down: <a href="/static/vm_reverse/kid_vm.zip">kid_vm.zip</a>!

    """, # TODO
        "flag": 'poke{th1s_k1d_cant_sit_still_c0nstantly_jumping_4round}'
    })

    declare_chal({ "name": "teen vm",
        "category": "reverse",
        "score": 300,
        "info": """
    Lazy teenagers, the only thing they do is sit around all day, CALLing each other.
    And don't even get me started on their slang! The only thing I understood was poke...

    Maybe you can teach them some sense: <a href="/static/vm_reverse/teen_vm.zip">teen_vm.zip</a>!

    """,
        "flag": 'poke{st4ck_po1nter_g0_brrr}'
    })

    declare_chal({ "name": "Simple Servers Real Fun",
        "category": "web",
        "score": 100, # TODO
        "info": """
    Check out my new Redirect as a Service website! 

    Website: <a href="http://matrx.me:5003/">here</a>
    """,
    "flag": 'poke{th1s_w3b_w4s_fun?}'
    })

    declare_chal({ "name": "Pathological Liars",
        "category": "web",
        "score": 100, # TODO
        "info": """
    If at once you don't solve a challenge, ask your parents to solve for you :D

    Website: <a href="http://matrx.me:5004/">here</a>
    """,
    "flag": 'poke{0h_y0ur_p4rents_d0nt_h4v3_4_fl4g?}'
    })

    declare_chal({ "name": "JSON, but not notation",
        "category": "web",
        "score": 200, # TODO
        "info": """
    Given the amount of rickrolling, I'm fairly sure this site is broken in some way.
    So that means it should be easy to become an admin, right?

    Website: <a href="http://matrx.me:5005/">here</a>
    Files: <a href="/static/web3/index.js">index.js</a> and <a href="/static/web3/package.json">package.json</a>
    """,
    "flag": 'poke{S4V3_T3H_P0T0TYP3_WH4L3S}'
    })

    declare_chal({ "name": "The tweet",
        "category": "misc",
        "score": 100,
        "info": """

    the <a href="/static/misc1/tweet.png">tweet</a>
    Recovering a full PEM Private Key when it is redacted.

    Flag: <a href="/static/misc1/flag.enc">here</a>

    """,
    "flag": 'poke{hey_there_some_custom_roms_use_this_key}'
    })

    # Robins interactive crypto
    # crypto1
    declare_chal({ "name": "Almost encryption standard",
        "category": "crypto",
        "score": 200, # TODO
        "info": """

    I feel like I'm forgetting a few things. It's probably not important, just ship it!

    File: <a href="/static/almost_encryption_standard.py">here</a>
    Connect with: nc matrx.me 5006

    """,
        "flag": 'poke{s_4ffine_c1ph3r_y0u_g0t_th3r3?}'
    })
    # crypto2
    declare_chal({ "name": "Indigestion",
        "category": "crypto",
        "score": 200, # TODO
        "info": """

    I had some bad food. Please help me digest it.

    File: <a href="/static/indigestion.py">here</a>
    Connect with: nc matrx.me 5007

    """,
        "flag": 'poke{pr31m4ge_r3s1st4nce_4m1rite}'
    })
    # crypto3
    declare_chal({ "name": "Bland RSA",
        "category": "crypto",
        "score": 200, # TODO
        "info": """

    My RSA's been tasting a bit bland, lately.

    File: <a href="/static/bland_rsa_out.txt">bland_rsa_out.txt</a>

    """,
        "flag": "poke{RSA_sh0uldn't_b3_t00_s4lty_3ith3r}"
    })

    # Interactive miscs
    # misc2
    declare_chal({ "name": "Boxed in",
        "category": "misc",
        "score": 150,
        "info": """

    Box outside the think.

    Connect with: nc matrx.me 5008

    """,
    "flag": 'poke{y0u_mu$t_r34l1ze_th3r3_1$_n0_b0x}'
    })

    #Some more pwn from robin
    # pwn3
    declare_chal({ "name": "Gotta go fast",
        "category": "pwn",
        "score": 200, # TODO
        "info": """

    People keep volunteering to be tributes. I really think they should stop doing that, I've seen the management system get messed up by this.

    Data: <a href="/static/gotta_go_fast.zip">gotta_go_fast.zip</a>

    Connect with: nc matrx.me 5009

    """,
    "flag": 'poke{s4n1c_w1ns_th3_hung3r_g4m3SS!}'
    })

    # pwn4
    declare_chal({ "name": "Green shell",
        "category": "pwn",
        "score": 100, # TODO
        "info": """

    The Green Shell is a launchable, which when launched from a player, will start moving. The shell takes 5 bounces on walls before it will break. This can be deadly to players ahead as they must dodge it. It is referred to players as the "worst" shell, mainly because it roams freely instead of targeting a player. The shell is green with black lines. 

    Data: <a href="/static/green_shell.zip">green_shell.zip</a>

    Connect with: nc matrx.me 5010

    """,
    "flag": "poke{1t's-4_m3_sh3llc0d10}"
    })

    # web aaron
    declare_chal({
        "name": "Hack me with HTML",
        "category": "web",
        "score": 100,
        "info": """
        
        I decided to write my own framework for blogs. Can you help me find vulnerabilities?

        You can find it <a href="http://matrx.me:5011" target="_blank">here</a>.

        """,
        "flag": "poke{h0w_d1d_y0u_g3t_my_secr3t_pwd}"
    })

    declare_chal({
        "name": "New Technology",
        "category": "crypto",
        "score": 100,
        "info": """

        If it's not Windows New Technology, what else could NT stand for?

        File: <a href="/static/new_technology.py">new_technology.py</a>
        """,
        "flag": "poke{Would_number_theory_be_new_technology?}"
    })

    declare_chal({
        "name": "Optimal RSA",
        "category": "crypto",
        "score": 100,
        "info": """

        You're aware that textbook RSA is actually insecure, right?
        So anyway, I applied some padding.
        For even more security, I'm also using SHA512.

        File: <a href="/static/optimal_rsa_out.txt">optimal_rsa_out.txt</a>
        """,
        "flag": "poke{single_primes_are_definitely_optimal}"
    })

    declare_chal({
        "name": "What's a database",
        "category": "web",
        "score": 100,
        "info": """

        What's a database? Why don't you store actual information?
        Why do I need to guess?

        Website: <a href="http://matrx.me:5012/">here</a>
        """,
        "flag": "poke{psych0l0g1c4l_ATTACHment_1ssu3s}"
    })

    declare_chal({
        "name": "syscall me maybe",
        "category": "pwn",
        "score": 100,
        "info": """

        I threw a binary in the well
        Don't ask me, I'll never tell
        I looked to you as it fell
        And now you're in my way

        Binary: <a href="/static/syscall_me_maybe">syscall_me_maybe</a>

        Connect with: nc matrx.me 5013
        """,
        "flag": "poke{Here's_my_flag_sysc4ll_m3_m4yb3}"
    })

    declare_chal({
        "name": "n % dumb for n = 100",
        "category": "pwn",
        "score": 200,
        "info": """

        They said something about maths, capitalism and conspiracies to exploit them.
        I can't deal with crazy right now, so could you just quickly check it out for me?

        Files (Binary and Source): <a href="/static/n_percent_dumb.zip">n_percent_dumb.zip</a>

        Connect with: nc matrx.me 5014
        """,
        "flag": "poke{1_filt3r3d_the_f0rm4t_str1ing,_b0$$}"
    })

    # PokeCTF 2020

    # declare_chal({ "name": "RS-yAy!",
    #     "category": "crypto",
    #     "score": 100,
    #     "info": """

    # Pay attention - state of the art cryptography lies ahead.

    # You have been warned, you are only wasting your time here.

    # Data: <a href="/static/RS-yAy.zip">smells_funny.zip</a>

    # """,
    # "flag": 'poke{WHO_s4ys_maTh_has2b_H4rD?}'
    # })

    # declare_chal({ "name": "Flasky",
    #     "category": "web",
    #     "score": 100,
    #     "info": """

    # Well, this webservice has a python backend - no exploits available for you here, sorry.

    # I can give you the source code too, I'm really confident you cannot do anything about it.

    # (the flag is in /home/poke/flag, go catch it!)

    # Website: <a href="http://www.cyanpencil.xyz:5005/hello-template-injection?name=idiot">here</a>
    # Source code: <a href="/static/web2/flask_vuln.py">here</a>

    # """,
    # "flag": 'poke{3V3n_pYth0n_c4n_b_vuLn}'
    # })



    # declare_chal({ "name": "Dungeon",
    #     "category": "misc",
    #     "score": 100,
    #     "info": """

    # To get the flag, explore the upper floor of the house without dying...

    # nc www.cyanpencil.xyz 5003

    # """,
    # "flag": 'poke{1nt3r4ct1v3_f1cti0n_is_w4y_und3rr4t3d}'
    # })



    # declare_chal({ "name": "Acrobat abacus",
    #     "category": "misc",
    #     "score": 150,
    #     "info": """
    # Well, I hope you are quick with your hands...

    # nc www.cyanpencil.xyz 5002

    # """,
    #     "flag": 'poke{Y0u_are_7h3_w0rld_champion!}'
    # })



    # declare_chal({ "name": "A GIFt for you",
    #     "category": "stegano",
    #     "score": 150,
    #     "info": """

    # I heard you like GIFs.

    # I made a special one for you.


    # <a href="/static/stego1.gif">Here you go</a>

    # """,
    # "flag": 'poke{sp3eD_0f_soUnd!}'
    # })


    # declare_chal({ "name": "Falling down",
    #     "category": "misc",
    #     "score": 200,
    #     "info": """

    # This time your abacus won't save you...
    # Try to avoid calculating the same stuff all over again, please...

    # nc cyanpencil.xyz 5008

    # """,
    # "flag": 'poke{Don\'t_f4ll_Down_tHOse_stairs}'
    # })



    # declare_chal({ "name": "League",
    #     "category": "pwn",
    #     "score": 300,
    #     "info": """

    # You are up against the very Pokemon League!
    # Choose wisely your pokemons ;)

    # Data: <a href="/static/league">league</a>

    # nc www.cyanpencil.xyz 5009

    # """,
    # "flag": 'poke{UR_p0k3mOn_cH4mp_c0ngRaT5!!1}'
    # })


    # declare_chal({ "name": "Dropbox",
    #     "category": "web + crypto",
    #     "score": 300,
    #     "info": """

    # I downloaded from github this cool file sharing app.

    # It also follows links! Since it is open source, for sure it is backdoor-free.

    # Website: <a href="http://www.cyanpencil.xyz:5004">here</a>
    # Source code: <a href="/static/web1/server.js">server.js</a>, <a href="/static/web1/package.json">package.json</a>


    # """,
    # "flag": 'poke{Wha7_1s_7his_CO0ki3_4boUt}'
    # })


    # # declare_chal({ "name": "Signage",
    #     # "category": "crypto",
        # "score": 300,
        # "info": """

    # I thought I was smart when I made this administrative system. 
    # Now I lost my access and my private key, and the only thing 
    # I was able to recover was this compiled file.
    # Can you help me?

    # nc cyanpencil.xyz 5007


    # Source code: <a href="/static/crypto1/entry.py">entry.py</a>

    # """,
    # "flag": 'poke{CrYpTo_4nd_sn3ks?U_M4D_br0!}'
    # })



    # declare_chal({ "name": "Curvaceous",
        # "category": "reverse",
        # "score": 300,
        # "info": """

    # Listen, why don't you go watch some pokemon,
    # and let the adults solve this serious reverse?

    # <a href="/static/reverse3">Have fun</a>

    # """,
    # "flag": 'poke{Up_4nD_d0WN_it_go3$}'
    # })

    # declare_chal({ "name": "Pureblood",
    #     "category": "reverse",
    #     "score": 300,
    #     "info": """

    # Listen, why don't you go watch some pokemon,
    # and let the adults solve this serious reverse?

    # <a href="/static/pureblood.tar">Have fun</a>

    # """,
    # "flag": 'poke{0h_tH3_pur1tY!}'
    # })


