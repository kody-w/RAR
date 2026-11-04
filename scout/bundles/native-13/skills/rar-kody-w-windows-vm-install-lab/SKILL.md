---
name: "rar-kody-w-windows-vm-install-lab"
description: "Runs an allowlisted Hyper-V Windows 11 lab for repeatable RAPP installer release testing with an embedded, hash-verified toolkit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/windows_vm_install_lab_agent", "rar_sha256": "fc726fa63a72e17477e2358af45d9ee652adf5496439df752362372f3b58f9af", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "RAPP Community", "tags": ["windows", "hyper-v", "installer", "testing", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/windows_vm_install_lab_agent`. The original RAPP
agent is preserved byte-for-byte in `windows_vm_install_lab_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Control the local Hyper-V release lab for the RAPP Windows installer.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `windows_vm_install_lab_agent.py` and embedded as the fenced Python below (sha256 fc726fa63a72e174…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `windows_vm_install_lab_agent.py` first:

```bash
python3 windows_vm_install_lab_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 windows_vm_install_lab_agent.py   # or on stdin
python3 windows_vm_install_lab_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/windows_vm_install_lab_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/windows_vm_install_lab_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/windows_vm_install_lab_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Control the local Hyper-V release lab for the RAPP Windows installer."""

import base64
import ctypes
import hashlib
import io
import json
import os
import re
import subprocess
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/windows_vm_install_lab_agent",
    "version": "1.0.0",
    "display_name": "Windows VM Install Lab",
    "description": (
        "Runs an allowlisted Hyper-V Windows 11 lab for repeatable RAPP "
        "installer release testing with an embedded, hash-verified toolkit."
    ),
    "author": "RAPP Community",
    "tags": ["windows", "hyper-v", "installer", "testing", "automation"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "external_prereqs": [
        "Windows 11 Pro, Enterprise, or Education",
        "Administrator access and Hyper-V capable hardware",
        "At least 100 GB of free disk space",
    ],
    "example_call": {"args": {"action": "status"}},
}


_VM_LAB_BUNDLE_SHA256 = (
    "b729b69e3240ef0edf63104a06d91fe48ac8ecd803e10b9fcba142b8170b6ee6"
)
_VM_LAB_BUNDLE_B85 = (
    "P)h>@6aWAK2mk;8AyAuA@CGOX006xM000vJ002X5WnpqHQekj#R&7jSVlHrVF<nzjZ<|06z9aD;R)_<%2FdE<V98QkyN^^(j39Cj"
    "6jf^&%r>x#c9%p}oB!Tf9<E((4ByOrk0D(*MGg8B;|1eKFX`G=NUf4ebafF)k%LlXNn9;E@H5+Lsici(TLhm}X^BmlyQPO%2#q*r"
    "v-lCyw%s>ab7muMPit0C4Kd|M@a8k}?&AkPOBvUhyQ>S34;AGbdNP~l?`_MsE!#>!2MI37^_?hy1bdK*2~M^+NNL-"
    "0KT9d(D%V(yB$Ob5=U_M_TC|RB-"
    "8M!_fZbgU#QQE74<f27;zmi5OV;Y1v~%VgwyK#sJ_)`EnS<f5QVMW{L3}&4Aor`>7=p`ddJ>&c{1t}p*uNcW!DPqe3&QhGi?T#`x"
    "<UF6tbuH?xEC+sswj+bFSs@W9dIQy;u#8Ty778P+~-D(8~1nQ4|%LmbFe%7f?Si|gV*lQ@SZkkSIwS)I1-"
    "r!H9Z7x91>7ooIz^|)Hr9TAQ;Jx6t7Umt}xLQFXEBu${S^eamUq+q)DIuS~PeSObL#fb`tN1*0)D4B&?|dWd3SfCBD(TA|7fWj1w"
    "cppE$D;>rpaXVt93W2Hy*sVNSgtL}`j~#;YhI=mN4O1uKX2kqo}5C&xd}?uE#X_rWj8#SvUcA=8$BJ;SmoSzLsc_r^|862#-"
    "wY5e8FF}k<Q|3<&|ZrE1Zs=QNLG@?&0yBX=OhY-vkH{>yt<MSy@qx(630Z>Z=1QY-O00;m803lEtl4#?M0{{R}2LJ#T0000-"
    "Wppi4VQ_F)X>Me1cXLT|Z!U0iF?CeiZW>7teMjOSN(fmXxd%gRuNDdIa*ItwY|BHEmApK3dJ5Cop6*dkj{#-"
    "#?^`_=ZrSiKO!w5~)TvYTGL9pKZX|Ui^=qrWtk)85dEBbkfPOEjvvj{~&iU78V;l^iG3o#P%#-"
    "AEOm~gTGrLb#dYiR#N!sspUQG~7VNGgQE)XW}tTsyOe>#8or;G-"
    "@ckiydx4&HoCFpduy}tVWLS)Ki76+(VmR<;xX=itXEd43hd#Uh&$LJG&p#sb%?RKZyp-rqzar(wp#+@{p^=|HaERV;wx7UG8%^}!"
    "EI<a0hheBZD4nA`!P^Wlq_TE^5^;)}LtJgwwEF>(#eKZjQ`;0avPndIusjJtTQ)`VK3Loyt;tDNlk)sWrNgDOqEKZDdjJz|2(E4D"
    "cW>4I$q4^Ys!pg+uoHzD#2T2-t8*N}EjCxJ3pv5#9{i=XAd@o9HYil-?Izb^<J7B-"
    "C2fiW#!Qz|54be<~2qnAF?ZSayz`ZZfU7Q9~(hm=+srb%hUMzP+kw;J1=fxeXlvGKI%&8v}X;C<1cjR=$LlGz#b3rH?zHfzj{`JK"
    "2B*tDEWKD8*lB?3AQF#aDy$=|3EmzdCpKQLRMw7t<ZrIFW4Eb}hOArpZieA9~!T1**Gshk>rK(mH`q}s78DsN?W$YqOmHQHok<;k"
    "}Bs-E8gjB3{YBx68Nu6QYg}pRd3vxT)^Dpf^gr>->DmyhcF=dIsUj?|uvos{y!snv!3PO|RrLz^6ivE-lg&Y{ONJ9%Z)f<bDTA80"
    "kiIQ;=1D&bA3F+dbPkxOQsdCch!*DVEYql6aPNu*#!qp!Bk+Lh1&ca8a7p)ABz$3#5XnNOqS%6#VK=^q*3G21%WBn-pJ|5aq06Ip"
    ";Cd8-IMX7r=Rx?>lz>3nAtma`Vvr-2Bb1+B!>K&DX>$}nUpiasX2)(aJrjTje()2ov)DF^^E7gZ)>m{bJ%YOfv7G-"
    "oAxdYw1(Ixb#+jpaKI-BX5_ik<pTg!v<gL2Q)HJs{$)`NOAmRO4+ydRQ7JMd<CZIu!!#*48Lt+i<RX9@m*dgwkm;Y}vA4i_>;!bm"
    "p{W)mz-n6L0w!!+83Un!--Z*U}n91)y;-"
    "1F(rqaAJBGlL@{$`nQ6Cq@MsIWb?TTFjT#htx}Wrb(8MU%wIIhvBPeIv&O&M(VZy08mQ<1QY-"
    "O00;m803lFVJ$&Ne3IG7c9smFs0000<ZfSIBVQgu7Wi3)+aBx;_OkrX!aC0%GSy@x#ND_W0g8xvf@D6qi61KtMW}_oUzQ8kJJhp+"
    "^1%fS0Wn0~nN+Xp3&ouvivksjY_pv+xD&<vKnO|m>?z*1s64r5i+wqsx+QaTnfJ5w6cXtr{+(j&e^@qv@o=+%c=p)j4r}q;a1UDY"
    "6Y5OI*G5oQd0K1&BLj0%G>uG<|ySg-oqx<xEWM1~)vSRBq32#UkIn?Lu4WrRAj^3f0u5hz;%*o7Fz1L}e7?}O$hm+=@)o=Cct$w%"
    "PZypZX_5NY~uy<T<4cd*vX0O|99G|q0+JkQUL!*5(s2?45-"
    "YB?=EZgyx*P+<Nim@O%Jvi_p+ciAL3TZ?a%&@3;VAE&crPw}**4~`D(E*j526-"
    "U|$L)64>~!kKt$MwlfAgNcY)4JtXdKr&&29?}JpRz=GzTBdy4gLfxBIPT{bbNQIqV&^+jX;b(mZONn1jYKY`Wb(?wIZ4MyBD}Vb<"
    "!QGX3lX(rugGDE;MEBieV#6J~H4yF0bro!y-&Vfqw|w%8@L3DT3Zy1<M?Y<H*94?`N77H1iUWI;mWTZHdu%4neN?hL(vhD-"
    "<U*d?g?D|LK*jM)lR#?z@4Isp?wrls*^1d-R!YDgc@&?4N1MeGatXa*{E)Ak(S0Y_p+L-"
    "e=YLB+9&&m6V}&398`#UcD}q>*XdLa@{4XsD<jPEXGW>&78i%c?acBgh5vh&=08^H0QL=zVeNLN(Q|WQByqp`R0J45Ohxp)RRzF|"
    "QLlE|X+nVPT^n_qE`Q-"
    "($*%J`SlxqR0%Fu?Geu?vVMMM%xW`V^XwiPuoL3Bl*Udkif+jslwtu+Pl~GYVZyo$~w7ICKycR=QPGq^h`rLJp$|oD?BFxF!0>6$"
    "zr*3K7ICl8vGeXEPi@^S^s5ry1oA3?EKf?E-pvo-zU@A_08=c|Nc+&@Tdi8`ax5|=4*(r;yLi8y9d;)E0WM(7EZext^-"
    "DwAr4k+Lz+2?y*UZbh);wQ!KvMlK;$Mz&cbzKej?I<!02%0RcV8wd_@b#$FBR9zUM>%jZ%@XiFLvNFi`&lA&-"
    "<a^aVj!_p!A~cJ+7WxVy?D`e*iNTo8ZBRuAa4cyuCF{&Au-XzGxh1*+;kWK#8QmegvA)toAy<+c2F*eayY0Ir1u!xj%P<V2wU&)5"
    "lxjTl81^%u@E4hcG62PD*Q46V3*tRj-1;V;!pho+Ax1nt6cQ&5!4{TDb#fg;p(thKg}w9Yz!7%P$u1S6_$4u8OuF7-"
    "Tc42PInfm4;UEzF9d$d)GQHmwOwi8Wu{wz22wHi?jB;;RxQSy4b%*tW1|L>rmEs=h#16p@QH6(O};BxXgbCK4eHnx6qf^z5yc#8t"
    "|rRKCZiUZ;Ej#KLBX#wo*4kJKJeK%c?yE8@DmPK)|BN0Zn$Bc$JAhasKg+-w!bNKZC=0m%VoWNKxKYe-XjBQL<1s5JWU)P>@y617"
    "6P6@W5&*YSpa#4s<IPyr5`k5>T)D!}aNI%32FVq!Z?_C{6CGK5ty9mt^6Y3Bf<r}xvV!R*$Y^zSc|PUT+J6EvFLt0I>~Va@1EiNl"
    "`63^2#&;y@_j_~Bvb1dx_UXf!mW0}P~w<Y;&v!v<j$yI=Y~BO#Q#h<xeWu_aGDg%<@anN$SK`zT}DN1!BS%)^ZVh#C7f+N<Pkt?i"
    "-2qP@hnJtG0bii_7YX3EbTFCn)t<XQp*X}$xw9Xd~BggxH4+zqb`jvlf{;Qw)=suF1kgfM2I<Mn;Js@-"
    "e3hf^K^QkYUbp7z9(E`;aw=()ZL@m5KlhM+J8ApsJXp+>!a)+u|@WXL5r5^vF22Q4^t9-u*Frs}_^|AGZ5T$SpbC-"
    "*hs4lU?9K#jA`K59Uv0D&M2KViqkbC+a3T|njJh%a}hj`B*J26hMPrGDkRjt_s;g4k>tn7XPKy6L(gF@#D5$v8>u{)j3I>_$ZSLM"
    "b#LV;M*UsaoIXHrZKVaT&48Pg=hE|LsEZ*N9G}b(x-$t#@-u-3MiWp{PfM*u+j;mbQOWhjUc7ca@`=X<2YI5NugR;o*h-"
    "$mLzjrq(f8lCAB+A>l*K5N#dk_XzKQ)QMeC3%h3_je|?MtcwSL5xIF(DEyK3Hb&7G>5SVIwE4LP=FylAdr~RV$)BjW@7G*&qAW^}"
    "&$R6yuuIWpUP>BO3f&zbQ?(NC2?H=WX+84UyI)-"
    "D0tYFt!3lGBLNJ!z3_ZLg<;95zfj6tMUtWSpUIMz8R%Z}LWlCB1#%>Js5zJz#$9M?wDuBfA8Mp}bARsMp&05V&NDWxR3184v%=A("
    "0x|<tCNvgD-#juoZKGRwWl5YRw<|#mtMLZhGI3w;-"
    "{|SoKjOrp#$yAIaIeEGnja}^cGxEaHnNP^FQag%sz$NzK40z==%$QM6R15<;zm&eJ!4ME&9yZXml#Hsq75@eGU&NH!b)6T_MO&Rx"
    "c4M)LN!`Vtvx9-QBXAw%ZTKCEzNv85KXAN79r=@1J-"
    "D@!r6@Ob=c68JQpRKD??Mmy`uHqS^bvdZ@saVD6KGlg^(J_fo|<SBM4Q69^m80#?>ML~Dd5z~L(_AUw~2-z;HX|~U-"
    "J{mgn0CcD2K?+XA%qO1PXoTt|8o@eTqqLMvIGgIw9e;lSIY})H@ap197h-9dS_X#SgyMJ^W|rKhe)nhsd1Q3h)xruR}-Lp~DGr-"
    "{f|29gz-"
    ">91CJ1g3KsQQ5K7_D;)LlJ3X80mvd6KyIb`a@;yovK%iKkqu4{96N%2x;OPQE2UV~jYacCnK4j`jLm_YhY(N{W3@=0v(tF@5n6bq"
    "SxG})<=&%jNR5EVa+B1$2XLfk|?LtF=FcS@CQNmts1L+(=o*WuS5}Acs=vw$C=h*E2)}K6%FRssqqsOs1JKucAu$h)i*$n*&<4+|"
    "5Fdn9i_b=3>_wH4w>WzjGd=8D3<t9@~8Xp(tbk_f4IO|^Z`XWN=1=qcGUm$D~1^^&Bf61PG0UaZ>>$y~T-"
    "FA2Kz8~KDI6Z|8(3?$y>WI|6>o<b0V*hUReWRrezuO`-"
    "wRr<#7D=`PXL0cU8giB;e;a_lhiADf^9<I?Dt;K<zRe3;K<<6ls94Tj&u@pgf~0L2Cwu-#Oe-"
    ")RK(7I9vi<Oj(%nt&%xsfgGfNr+bUmP-IUc|Ah2;@_hK5kKNmY#|$=an}5W}!6=9c6~Ay4<}a(q3LpIB6buIB8*&qtJ-pCui?aJC"
    "WJL?>R!`%{J9YTPc<s^MD_C9`#zDA#^V!tA3_kucZN^A#}y+^DH9N5;Y=L?@-"
    "WETJgPYm#{CEPaU8GO<Y0@BeIIh&csZ3ONHEY?Qm^{K};Fc4(^>W~N%La939ROqP0K(-"
    "oQz_yd4TV2b9CMb6i}IQ8x62gE5(B`rzO(vfexsVj*qC3#U`(Y|jJSY(wcc?*sv;tuH7h~HlgeMlsAG%8t(;CxOaCaxTkWKL?%n>"
    "zq;F(yciQe>ro^V7CZUStVVEsVJ7w=X_Odc+7K@d2!SQMGxND_fPSmK(ptq0c9-beiV950MFFB-xV!#+>jO8qIm~b1nu$!W`OV<n"
    "Xyy+yx0|3&q=aUQ#~;Neg~jH<w8D;AqL6|LnkGC^n9;n&&LhE#L(>N0{LA;V=S4y5p-"
    "0ss8~`O9KQH000080000XP>*GoOxzLx05C)V02}}S07-6kZ);^OQekj#R&7acb97;BY*b})bS`jnF|{0NZ`;WAy8-"
    "`)0U<Qf#^l;bH`{vQVr5xAT3?W4r+{r3G&!<ZQzXknj@tEq?|XA`W=J`5l4`MuM9#cp-Z^jH<Yq7rV_NP<Nf;%M-"
    "QL~iM&{@Kyt}zU;B#~B$5H5)bWF>xGtFr+bGC?+<upo)(vM>r;_sa1Rf1ot>@oL4>L468zbJEnd)FBUH1YE&C3{4Iu}19s1wEPjk"
    "Mzt>qA4v(d%%chX%Uraz8s}#<1J2)qlAv=)P8m9Ki~{ReXx5w^0VxE4$m4CjGv=2n4SA`x@B=c@{>o}{j|NkMSlITz1_RJiIVcJb"
    "5sGDBkG6CNi?TvRgP(pCSd`Xc3_x<@{p$SUFRQ^0^W<{(2wFOr!b~d=9NNKFywMrKYsR?h5hb4oy_v|d2^$;xv{wcB5}t+dQhIFA"
    "tmlL&5I~a$SDw9l$#r!VV<XXKPchhWlpCwr%8Z#opG6F&gRC+JWKP^h1pe1N%!w*l(?6EIU}9R@i@q%tYpjPs1@_FV!q?_h<ljk0"
    "Yw_3De1Zi46>xtBmd>JTh9Ue&B=v_SnhUrk7#*V#WDWsu14>9x1Q(pfae!rssXP%qD2}nsF-Wf!BD}p*k6KtU^w7(ks)B`ls|K&e"
    "n>^x+~^kt&H1?FWk&Pseh|>2Fgb20Y|V7cL?E9Ftb<t;hbJYS6G1Ac$zw1ISkx#kX-"
    "=F6fa^y1(EC@BCJu2&G^p|dM65}ajH8$)WxO1uNf{*-"
    "C4X?__!*;IFCP9ygA&xCC_m>>Nl{0y%7C~Bv;b>FdpG9L7>3JPKur#m@9_6E(<Wz%WBin;o5VR!335Of2V^eS;Mp(8G_8`5!2iJJ"
    "yH3|!fZjWgjH-"
    "m3(`UBuYI#BHcE}XT@f?orMJ#he0%%kwg&ryxnl#rQNe&Z0LwA}ImFmMd5@Lk)hJ`04EFk%r{6XO50yO6^Pv`F6L3o<JbSE%YAVP"
    "2+V!NJ&UwUd4#R}pJa(#U8PZFk}7&w`JiHdTUEt)y^9j?g>M{{%Fb18#qfuPR;mit%|{qdy_dL&?gr$k2#%9YONpbs?cmoTm8^~3"
    "N0yifPTFAdTrGfL>fk1L<)peE?3AZ418G!8+`Iq^vj?%00-"
    "#{yp{j(Y?$K*aQ+0y`j4Nv5z$Fc5S*#|1qZU;KDx6a&lz+|PcVpx!e^OzKk*9Qm|OLSP-"
    ")@W?orQRW(v83vv_P+$&*mj(IjwhKe`)rg~cRB9}6i>adu(4zlDWo5K$kMx;c)VAw0{+77xy*~X_Z_tn&^JDHc;jsiXsfP5<(lf!"
    "r=Ek&2ICN<yT9B3CdA6Wp=)ecZf+15xBNnNo3(<o#E=EqvDo=?1SlM<U0gdS#U}4}8Ae%_Ul+u61(EEG$PvjBQ%N;bL4~!tL8v~E"
    "vW^*5N7&><sKY@>R3-FnH?qU~2ouIHZvQPWt$?%^ilflKokhlpY+ii|-kXE4AY!#DgPII77={}NXc`sBXA0*L5x=EC9`VGLHl73-"
    "64c>U;>VYqES0~-^PHFO3&U)Ic4DBMsc?meb`UNv9xrn>FlYA*G2+?ej8{qs-OokW_Ypg)IaoLcFK`DNuG=bRq#f!nS79u1I`Vyh"
    "pfvC%w4`6H|*AWCPv&yn~NpyW|DlG;Q^tpo>4W2T{E=p5pYa*5QYPp}8876*K%+itv5`3lf8l7FY<CnlnhO*lEji_HP_>PbD@AvO"
    "bwaJ(E64s=G;Y*X}#;%h<41z320J$9mqKm3@&kgC<BGRNo0w2ABMFvxP#RUB~`H0rah4*3(9hW|&8siwUR-jR&zdPG)3c#e(333{"
    "Or;7YoOU76tJ*eNbq+}h~Zp<?=2ZI31LgzkM@)AC0XJP0bAJ6AS;o#tEI*q=d(>SW45R@I10l#&7-"
    "Xt9hGdg#AnpHt={|ThpS<HoVc5<N1jr|8#?Ot3?g)87ACfN9hWI{_|MPdW#OhE)d97>BSE?19cuM6TxBpOzQZZU7pmn1lgISvUh&"
    "pe2Vrxl|@cy%kN@)nRpuu0O|UIDMh-~<qRH1&fPb~HAfM-"
    ";3p#}?jyBHVbOW%5KA|C~T%A_q|pX(#w;vAGaAa(A4?k;t0hPnIXt4EDB&N%)q5UAF?Y{HPOY4sM2qcfSk0XG$zG2C27uq?v(ex|"
    "2G>;~qvyRLsoDhUZl~U+n_}<YPraSrvqsgB)0TOjktUxISZ=X$?~P#fOY&37!>vwmxL)$AuVyE>oq;^$0zg<pY)f9Y97El}*M@WC"
    "dW=fQARR2k3EMqos)=AJ6;`zkF&AfPHOF|6N58<7v?b;h6d{sDiy_8j;H77TSQ{yF$FoGxeqZw#;X~m#jd*U0wlOM`T|;29bfYgM"
    "|q-"
    ";b`HYR%&=J_d{wm_aOvAU~#S7#?EzIQ2wkcYr`^4MPTAa;n~98(?)yz*@_8Lw#E!IFB4O2VHz{6momDt1Q}JtTyz$olwo0nsw+=M"
    "0+sW`HQcYkwB@pHgPm2(7(~6|E9DTUW!euFszHl;6qU$NgKu+5P#QY>d#fhANI4+Aup^a~i#o&zr`)owCGJ5q<wYk}X|Pff22tfW"
    "BIpY6BFMQ%G{H0)<?(^IXLJr6Ghbb0`%5(VF4o~b{rQe#<^#_5$xmeGY#&lsptwP=wt><&Q#N^~iDIEnIBK>hyUbIp2Z7<c!YL~b"
    "U>5)}s>=(6jI2Rcv4=e!0;jb({a^{3k0{`;hY4<=L&Jab>4#B1e}<KB0^oDTSTUmes4^D`OU%U23FLHGAt7f`kf%jDEk8#|m_8Re"
    "^ncJLa9A=GYhnP&ou+{w>!XA(WVm6%<nqj(r^C0U-"
    "ml6OGPx+woUzF}tgCv(@&&*gRxIPaNN^{hKrsCfx$t>f&QSOCw`nF5<r&yf`kY7==b3DSxQ1fX-"
    "u$y4@$~gFeMZMc<Cq&}i&oURt)2n9R^51IMY*;aYe!?Pq_Hn>FlK=oxj6!KEC;T|z4v>~u`&QJ(kJR-"
    "1i<|uC=zF0t%A!dwfk`zJn5cy{S?m`=r#GqdW-"
    "$TAkCHnAS7W8DukIUpUvGV_aX<dVo}1~h=J_39{<3`JKuy$g|4rm6GtXk&vdjnCOx<jxz?gV&RmmSHQeC##i-"
    "DjLDe|tF(YgJ3M}E9)r5ii+Bt<WIP-"
    "%iRxigS&4GC5!T)&lbh#{NY2t~$K6*Pl_!M3qR}WqgM^4X#RM%ewNLGW9;2YHq{5*p*p(T-"
    "gyKWS!8SsmK@zM6(g4N>S3+%L*Lj)s(I0g(Zq7t;<^@D(BrCX#Gn1Sm*=9JDU8lrk7fNJlW)T~pQ(m$g3BAA%^5xQ3_UnmwJ9L}%"
    "=SdsuwlnmgW(}Zf(0<51Mnk;rjigYtf7Ezui$O=FB(H>lb!r?k~9UP5PI|IRB^3)^miSwI7-Zyc-"
    "5#m)rb6W#$vLdJohzuz^^HAGC{d2@OHhV-"
    "C72So%5dT<lV$y2@;X28IWc+&#=fmIrwDT5VM|?NKDVn{VAWcfzR~Z(}4b`4*=a#!rbv9xAEOaSfs4JmeZewe&&TW<J+FCI}<ln1"
    "apQev>et{oVnqz$ZAScCn;PF`_Sww6}qWCFD>aFYNWYOOCb!b4N{^jNU$@zHFKRvx44KFY5uSTaR7>ks(rjCY(h;Qyk$yae*4@cv"
    "Zi*tplu?=dUc7Abx+P^v<93!F~8%vx%Ha1OG0$?nmjqM90vL#w}t!R5IqHI-"
    "8|DuIjTOnvZ;l*`4k3Ixn2u=hOuYMfki|*>sy+v+tgf~pUOQH(y?p{p}|6)6r8Z0|{l5pF2*s`eFB3;a%gdH<vh(RLkvi(S}XJKr"
    "qC*ucP4yLCCrl%ethm<je?0FjDc5}#xL4{1?C|HvHW#$+BESk12_fO1SwMUo<rJC~*35k?>b4mw8%>X0Ko*8Q_hef84&%|*ncO%#"
    "+!DgOiN)P}*X07(}>RH)0K}A#gp-"
    "`p0{ZOE_HNF9?701^JlS56CQmV~Sr^5Q#F@2j>=&=cQZTVw`(fkz8>pF(ltsQQ|QLwZ~+N+|gJv9<35%V}inV`&#>~yFJw&y|2HQ"
    "opodwRO0aV5{l+C%E<?Ld2sb+x?z^;Ey^4yrc|@`)>!ur6A;k{b|Gb4RAp^Nk6AefVb-"
    "&oGu;jfbPl(Z%7(>5w>{8hBge!7ZN0+^a{HUmt6&8RG0f16^ZuAnT63Ic{g%Yd@}lZDujoXJ9G&_m`s~P;fmwxF26!oqj704_Nss"
    "g5mk~o*kXm#sKL$Yzl4{^ZVF;xQ8SS^4kRs@7Z%NTYeRL|7dtVf%Tu{M&9vaspMM~ud$`pG_O%o)l^TtdtLWh_Nct~@Vl(#`-"
    "x^mw3Dosva{gbguHn4%@!mw(cza2oG}eAx#$^Ky$N95P4)k8m-"
    "d}Iv`)_Z`_^+1I!An8Z58HOD<OChqafezhs1nmrN8N9azn=(!ng?K&ThRxTQ>;td5zfg8j_FeVtIKB!jKi{)MnLM_|uC){}f!wL4"
    "VRG4rGvzpohgRA1?m-xU+N1p<||L`8Fg#>w(j;wbm@m1z-"
    "t|F=?G`Z41*f=nFovs{{wAI+y1d`(i#%7zlGeQqEC9ZqED!JT5A<Cu_{WyAak%GEMJR$<-"
    "S(Ez=VoiiPeKqw6+CjZ3o}$0LAwTp`z>-CZ=1X;8Xdz1#8Y!F1$5_q<6S&AUDBm|qF2yuGL?^0jcv;JPM49%ff!tTpnRBW-VmP`;"
    "KpYv<<pscTFF<%4p%a9Ix)IUe>8B)cY<BMk=mo>G;t2m_F=|KC=#Ix<h+xe@6u4U1T>wladvu3hU=X2g$+?Y+z(jt28kBc@&a%|H"
    "|5iP!Bzl-w%S@B&o)2K@Rk=zHN~vB83`MbOviZ&-^7<$z|`BAWyeYno^ZIv`HOE(efl>=#d4{IB~U&5JF9^+CW2-"
    "@+8^bnzR>@+c|0@6xAtJ!ge(U>ABrH8A93ouKZkQ0CR9nSAdk2C66K$bHGV+Gwh^XePPV7IS4wfy&^lPKL1VmZ)<(qg{ge-"
    "o`t&8*MaLwDpuKOeEklu>-sTucvkJ&RIiW-"
    "9Um98kpW$y{L7V)M0a5aq$ee<(;PItwS_bZS9slJt5DSVSz;xn2&l&03u~v1pMs1g-"
    "jiVp~twUPWt4uArqc0l;f8~sCR&;pklwj&YCEVZNqZK^@YG%GbW@m6A>l17?WEBonASkga-%01Ia4nZFTuZk4szSzR~3-"
    "Kk7(BXY5F7tZ8!AsJ6sQoktkpW=(5TRy5;1S>L}0s@=jC=@^!;?<0yb<X3;J5{dG&d;r_MnbT<AEH4|=V1PX><E<euk2e&ERuR1*"
    "s(CZh0XdrQU&1EzbDBRz$)ncoW4bqYM0r9CsFKjnL*5;vSZ=)M&1#Z02o^;#ndOzH$;}#aC!~HT+Ll^cBKu(|dK9`lAGR$AAEs@I"
    "eQVF~hvv8y1#LzYD1DYD>{5=<qR;eU#3K`NukwgEv$D)~fBt#r!>`^p{I|3F>-"
    "MiZKXc`S#RXH|_lqdN9(dLyQg>XCU)r%U|06Mbyl0bF7a?5Wy}(uE;zyMJ)~TjiizTt_kv8P7Pv1|&rTD5(7b*7ZbA{@jgd#MvU*"
    "1Ve7A-"
    "$7?XOxMtIqS5cYK#6&>i~)R$K8(!t3YS$~0KXR+evN<yL~LE4OQ$XOrg{o`baBMZy~q(lYFW7@HvB@F4c^rX3j|xHveaQG$0yNx{"
    "v*C?Bsn|IjwKYb_R5erkVo66!KlcRE+B$BLAx861Q+)}9+a%S@z>Wh4+WL2oyFOQVy(M#H*k{wwWH?K6y;=i9?lXUdY<_UoQz82O"
    "183*S&I;=mh%1u8MmC_pa3ELx}@N;X=R4UD#+7IND9^cyN+-sM4>-"
    "ndfQZe<PhFRL1&@OI^jmZ){O(i^0VYYfet%If~!Ya9P!?+!#SKPVZVrP2^DCYkqanj?7zYUwPG)+;i(GvFJ0b_jFM_u$yDaR}{Ay"
    "s3u*n&4@Y`>ZAkL%B@qr!6_QYJO$cz{E{N+XmOWe~6!TuR5)2W5mVL40YxGrq#`j76je9nt=!}D%lQ~t%*=HgD-LTdO2>Y<JS#a-"
    "gJDzJO~7%-"
    "~4A=s;;FcY*Q*UMcmJ`{!xM6Y8moCfw<Z@5I5ql8*RIgLyDGm+1oAy0hU=zM6KHr?M8}GnXCb5HDQ6GjY4kv>LxtzAXWYLZ&+?Ym"
    "w9hz-P=C=7BQ|C-tLAVnn1oSY8>){QL`MQ--r_E+0Fi*ydjeEynU~c9g3-"
    "H2)`a|>jmz7g|E?tE&jO(`zA1!NeM{0KJUg0^I{Xci^-Dif22F<@%xqk15ir?1QY-"
    "O00;m803lGez8sZQ3IG7fBLDy#0000<Zgy{LWi3)+aBx;_OkrYBX>et1X>MgMaC0%;T5WIJ$PxZ-!2e-"
    "E2#wT=#QEAB4gmthk?lkWztwV_4~}81$(6JT$>l9cJ8I(p-"
    "kE(NcS%WcleULeA1>x{c6MH$nOWZTBui3Oz2<qs^Tlv<v%6DJNweYZ4uRkGIX<w8$>9mj6IuzmA}`6Hk~KqGMRP?{4zJjZRl}fUR"
    "b2#Q5+vdwPX$eGc`5MuuI6cSdq+!#PZcXG{C8fbDgGO$jOMVhVOmxa1iBgQ#}ya(xU+gp?=FO>K$PI%#fJ-"
    "86jvFn1zoxeR)~_L)JWcaJBwLPB^Q(O9y!e=E0^O!GM<+eO;eVPC6jeNu8W1F32V4pg)eBnV8gvJ`RgywM>p3zuWklsX~N{?lI90"
    "=RRY(&zx8CQ^J&r(r2>BEv|9Ew6$@|qfmiYJW^kCYd)Sfe?u>SKc6Y$^;S6@f)rm+L39pze!EEH1qM>(p28U7#scm^K*_=t1#|)L"
    "8RiX%Xccxh(WEH~hI%Q<|o8Wnf=aRwsY!*viRLb5#W9q0Vv%O$M!XqJLhBELu8HPC!b*w%jU$pR@bvXTcdKTd+H!ohiVbu}D0zM5"
    "lA0I^@q9_=F&X3-KXj11Kd_?8G{PY-p*?SB~2&8aAcmVcLB4-r1t>AZZk|g2Vw^>$}!Dvjb-_$$-aZcF-"
    "{xuv$mtv+|F$_+FQ8cUXv}cAtjmfWCjse8T0hcT`+2KfU<20ZPmRBJVmLIfuU~@PloK`F&>c5w(f{~Vuwkt7wyc52Xv$_gT!CI~j"
    "ng{|rI8VMj9-p8@qUd8O@_=~uG(o30nZLL3DR{wBp0g+w3&m*woFzo(zH%}e{gP)4%=)g1PsIb8jQw6iWU|EOAm+-"
    "ep_`J?tVlT^${3>TD|x?!m<`YFKEk0W)-8D)X^{;?kdWuV!ABN|Pk=45=D27g>bxQ$`<?vML{7Do;(-"
    "JpHo#F?5s@=;bwVs2NK%^ZgqH+)f(?==&`|&s;-RaM1{IXY#T9&3(1L$hbOCh+JikY5=@?~=vDO&`eFrw^3({Ds%ibDcQT2`RE-"
    "&i>L4hUfZBV`-gFZ_VeuOX~&&K50$XI4~XI|&pNAD%CSa@#YMFpun)-"
    "5|dXspX|`v!2NtkcR}IiftRCDSVk5!JE^a122q0hL*D^Xf~xNuz}Qy)>}VzBggjzSj#affmdm&<icWxfC%gOLGbkoKFwD?K(#wDb"
    "(90X&lTE7#4QNy8^3DyQ803n|8LyYjyRYxFxiJ)#zjv9I+cu8;X8(I_wO1wCwbPD;fII^@3Vx2~_2B-"
    "Q@ZD(RdmF6k?Ss{0&<4i>eH(n-"
    "dIQ$wcJ$Ojeg7{H;XTIA8@xxc3}hVHt(j6~m;^NY^qB5A#@HmqgxO9{sABo``#9FuX^807l_CRYBz7u`QT>Vq5}oxSwP^=MeYUXE"
    "oJ~Cm;^5P_ye9i)%=sRdfzcj(I`T=smP<;sJt8Q|VGVsU=kSYG^`WP*`$cf@R0R#%6ZS!mv5t@RHEr$=qQXP0MM1AyPKnBHnB0{w"
    "hrd5_*b`y0-XxEf6Gh^6bk+ouNNGm}tNOS~2KEJ;|O0&&XeheiK2Qr!;0mSOi4+5Ih^fJ9y}xiOqpA+O!mn?K7J5Ik@JCr-"
    "&npY6*R;<MQFUav#%p$v$A`iyacE4!9ZoIf4aKZbPRbBQxNhSLq5vkLNW6sgrKlmKk>)Lrqc$iaC!MfH4M1r-"
    "IVm!%`r(yWo5YwQNtnS9QQutHFIwVXLf325(1%joK-U1th$n4{b&rNs+0XYWd-"
    "5DzvqIESJc37dDuhV;{Y=wy$&5>umJcYZxki*kwF}9<6l!g|kYimaWq+FuvieKh%4=MeDfGGgX6%|3+^%C$IG<df;lAd>(yUl&@q"
    "TI_?ve-GPn6Q%H5l^a2iCDIrb_oyJP{wMys>visp;NleHLQo0hgH3CjB;Phj?7Fz$eg>JAEntOS{XtGi**ej<oG3=tZK&D`Q+<*5"
    "5E8+w?4unpcuAw-m@h2wNyf`c4gl7xW%Jdt(o)d0Is=*tWezer1Ax37?v#2)LjOHYS+A{QBs8-o@%D(bmgXm5O{loNjzZZYv%-"
    "^=2P&XYk+Am9Ryz<yvn2zMtevBo-Km>^?jKUsztu+DORWzvbXeZT88aU?lt5hST+HL1=4?Wj)x1s40gE_P<(D_3`>;45g?EML0&F"
    "K$Rj})qvB6kp*)sm4yS3#UNP%vhWje_=6_L(>MV6ttiAP<xSPAzWdLf+Oiw(Su$g;viTE&BkH5K?ds(g$OA`S3HKp}J5IDUVm^(b"
    "ubj!W`|99jT3ExW1~xd_NHxBy6Heg11x0672Oaf%Hq0u3I=83ZJLn_iowUxx?_7I78|d4i1&S-"
    "Mb<}vkf{cp1|s|V2hmU>cbb$_L|#-"
    "Yi<jCtLpZAn^n!#fFBAbEQ4kMTa(QL8_O^C=wo@40;W}2E?JsJ?6bbSy2I&gABM^I5Ug0W%kpw5YZ6*Pjv+504cnmAV`o6zsYhjo"
    "JvKUor-?||M)>&G(sytR9AlUrATpy9H~{*DjY+BN5Fkljs@p6x`yo8dX<9NYQX>8Yvm2usuIi4*v7mb2zldqtm&mz<i9ZF-riLlr"
    "wqZ6x1AbPpeAuvr5X6Nu2^9;J#*jqxSN6b%Q;{=kSM9pXMiV>u*hw$kFMw6zT~aAg)+*m(^H$@_I?n;Jf@ZLndTMM8g^T)Xv?*;K"
    "GTYkcEctx?wB^oonsY4T{2wfIuRqo8XSaR8mZhmE?O~6ODBi{R_eo^?7(4sHSg}zateHi1cn{r^66%-(E|qM(Y)--"
    "MNe1HDKC&5<e3G_30NPQPfy3m#rdvlpB?6=-"
    "4(1DA8SG#?gkD8lqfC2OvhJS5{y+h91@cm<ANltm4%uu;e}4XpCDTt^RZ*RYRYzUcHX=v*`q-pc&jwG5GQ222PoQb0Y7Ekjc-"
    "5S;K8RGG*9#vEs&ARR4IrdOjm%}_sUT{<n#QmhqW1v9^bSS<tQ4e;TLRrJHkf3Nb5j(2pX$^6UVO6Yj?Lf+tt9`vITAacHoBiW!p"
    "4SnzR@a1{<vdXhV7SXuB~kk{e3txf!*>cpyq$o>U`wFxe~0My|A@xouGQg__8K|w@e)CAml%S)V*@$sPO*-"
    "gFl>+YIf}3IxBCv%jZ;<Y^Wprf~ij+7c7Q8A36hbe?3}nm~UY&{+@=r_<JJu8q#m$ud!oyNrkaRtfyiy{(cO7HwLY;<Ws!ckBLm"
    "--2XB<Dm4r&{;}|<Bx!JX?Kdd<YYc$V(o?-puMLiWy|g~-6HSZ}6p^vW#(tu`czr@Y4yjzEtWxuk`G8{-"
    "g;B>JtOj#4FKw`ZnVgI&TW2abJ^lofht8?nXlADgv-"
    "<Qakp3_?cRwoWz52t`;8w5Mf$k9+i=3wE%DWEg4L2UT;s0adj!fOWeRMdr6PtfA-"
    ">ydoyoB^&_T!EoFaHTpO9KQH000080000XQ0|xYeFy^p0E!0y02=@R07-6kZ);^OQekj#R&7*eb97B%baH8UE^u=(l~i4C+AtJ-"
    "N8&$RMQ8)9iPk+<s#MypD_v<3Vf2CV;3gMv7u%`rtV3J>`>yi^1hlDn0pE|~<9m)hyAW}L_MFR@%VoDWZ?{sWndr7#K;LZ25*{;)"
    "A=<9D&}dfP5qPOaE{$bLg0Wj`)R}aDvUI6gjGn{E`;FCvJDbltVT6)tuHY2T-"
    "UM~D12ylQGlK)cmN;aRFVNU#!5C9zxK(;RR%$Qn+7m8ujEiRKmOZ)-V(49-d>^wkoeGM1Ro$af$-"
    "MIwk>dCAit!}VNYx#yGi<kd?N+-"
    "*gYrYdi|kOv2>ukc;Yz|S4bj+ktMgfFrTdYk;7H>FHOk0=c%fCP*KQ3&s<ic~J4+C{H;PMt#Ow+>qcDs#Pi@Z8tLX))5yxH+{41p"
    "+bR75sy7jz+3zbO=K0d?89{etjVpm$dfY-N>ATt(}M3@etQbL2N)Zzv-"
    "K4)BG91y!#hu@(pZ80X+vr9VHgbSRXoP4v<oqC}(X`3b1<Vw>}7D^+FR>Vm%fwT$K<Z414rk9yOS#*^__tm!9`Do@2Yg1N9w^vps"
    "HkD2J>dHo9({ZOJ`MCD53)$V`wfM;gzvoXn<ktCuy}X0k4{k&5I=X?kn{;4}NRwRY{sXkiOhu?#mH@S`A5P)jKb$#`Kh+QP3xf^{"
    "OHJrVWK`$VvwF|UP6=D9%rXB$m&dh{XtzbouY}zQ>D(t$$Fa0wFi~NCgS+0EzTq&A{p)KXjPZJ|JQITHwKJ>IG2OR#UKuPb0Q#1!"
    "3x^Sv!*I1%TynFjiVr#eP#5iBGqdrG6XC2|Px22utca0+|M-"
    "NFt*U*xjb6%(p(nA|xW9D*UI7z>F0vrU=8<C0QC_gw^Z)x1c4NQt%sKE|koK7uNaM1tzB?sOZh=ao+)SsiWvs#(LDlUQ+WUghoPP"
    "yRMoD^;9yGUw-EJrV{y?UgEqT@Imw?+l`Inf|&+(@XgYxYxSHYoEHJ;FW$|((k-"
    "Z&WdN29~fsDVPG0767~zfI$P`K<m0P)h>@6aWAK2mk;8AyD|_-bOPF007-"
    "2000#L002&9cP&z3aBxClb7e_wVP|D7aC0%O8f$agHuAe>^dB&+rlRglj_umM#y6R%A}O{SzebXk&Nx0DO~MjmzK#H;_)`D(+XX-"
    "pA}J?rj~|=}*cTT2ChrEJ7f}Ark32tGn!WpWD{)dMG}|o#&)p6Fpq!@Wr4xA$kJD%JmUMWU(cb+X<0)X>cg8HfarkOaA!*Cgm2-"
    "G}Qr)<49wu?jfs!#i{WNisWFEqrQ6msKOL_$YAmj#Qj5o|WIIw605+$k6s72RKU>zQ>4r|CCCHxi*wMGsO$f%$}MnEHTxF1I~BGZ"
    "k}-Bpf0q>oM(a3WU=;JFj{pc^`Iq9rvC_sGEsD94ZZeP@tlgE))us7KA<NBeJ1_Q>JU@jnWrOB#ZnFW&*u&j)V~oAHkK;Q_>x!-"
    "J!v9CPTir>Xy6DsWGZkAEsvFGRlYypL0twp+b+tKFJXZcX8!F29UDN~}3e87P5V029XBt<ES-"
    "<FxOhW^PjYNK+cQLJ?CQCq}z94wE?L7GP%qCFZZOA6aM!q;oT!x~ZRVam_|?!*;^L1EWVQB}Ti|XN&>~ggAdrXgcq^E@cdu2hMYx"
    "q2kV{+z0#%xn|`Clv@&jyD9a+E_^4@P|h+q$e`S5LQE-(gEjTQS^?9X$e-"
    "#Q%CdVl{%yDXM`BtL;up5vBVVP8%Oxa(61?{VdhW0lQN(mkRzFzAsn1s-"
    "nV$ENj*X!0){Eq#QA38I1Gh(vf8Fg{Zyf8fZ@s_&dUEvAF$(s4mBt%llxShbIC-"
    "GNAty(cy8=gc!Qzpdh1+QJ)HVu+;#lSk^rfVg`iFzNPc-dS`N(DBGZOlYfv*sUlWxbXpml9B$s#h2eAGW!rls4$!FTY#X0GRl%bE"
    "bOT({{Lx?74I`HzZ$w>Q6(ZcZ%W{(2~|G{+!QxaEik&x06jEP}XLl~mZZH7C*qLA;Vumv}K{1bNagKI2Lduu2a+S%fZS&BNliCH|"
    ">d6ySsyX{dJ&ehOI9P76AApL54uQBT>I23(r3&h-"
    ")jzReeno3Ys{&4lP25=2gI9S4~RoEqKV#cAeZM}hef<4zFde9I_eDhl>6_1E-*a<t#S6XO)D-"
    "e7SCA%uNW*!IQ`4N0)knsg@R4gDYaQ|2lDFMmo5Wh}E5CFALJX%{Y-mE%XG;k+bHYs(;py)8$_7txPn;=Y?wH-"
    "o72Y~MhBbN$2#>^x5@sQc4XxS>IoLa^s%Ptizna3FF;H`evTXX-"
    "*C+)1ujFbn>@QZFSvd(6hsBo3(gifr#PKj0D!#Or&ZAAz%^SdLWg(pfux;5-CWXqbVtzX)g6i-9dm-nx*IkPxy~LEv@5RaCjy1;m"
    "yxLZAp%Q4Di868OXv)2P%bB*)KSfyC(Uk*={#P1#6Z#rWbh-"
    "I|<TvT>yGJc18<1gLRoRyOJ9Qb=re3iv|CuB|b9DJ<xPJo*tRsPO8Y!2=(N7UB1Wjgo-"
    "~cMz<Tj1T=3G$3nCt(Z{3TwQ5d70O7ac~^x>8Q0u6OrXpK&dSM4B)w{>N?|-"
    "WP+|&2*`FDdhrNnx%W{fXP#ag7G&%P>AXnU)c3n=8QpbCiIe^*Z7QkeQM0iY6`T+J1*T^fLjfOo~!Pc15knA`ERv{R-{${UN-WOs"
    "`(9762av1r&lpW+4LE^|={wwJ$z-"
    "cES@O2c3Zs5@gfS?j;0>vwoPg10UnLJEYxcv6T`NkdwsI$!Xz{erR;Q!2?J&UKJ7B`J6RDTEDbqPOTH<hUbQWu!h2kmu0tVDpmik"
    "67##X?{}!hk2wgMVj`&WWyHX#$c^Rk}S=a{QfKXWY8Vf&k=jBDSGvU6R`IjDE(!r5s2;k!ODigZvZ$ROxm6?ZR80<5QJ{o#P`d2{"
    "ThG-$AWx#O&lLwO4LXlDUYN-"
    "=*2o`itAKgLo+j1(5Errr5+OngrP78d`++X&j2GO{57bje=NPzqBU6&M623gENnq>m+zQ<(9I|EgHQ!mcz=uQ_8b6(voHVpHV<VA"
    "P@E_shI`ZOL3)n@sF+quw?tL-~^kVoqGzbyVNumi}7XuY_z!QUyc?FV~?0W5>4b<eD5_-"
    "IJ+H9XN%kEXtIlnrW=Sa>Fb1U`qSyh>&dW*(AEX@da{qqkE^a-GjB`iC|`oO6S*-"
    "C8_4bK{m<>z9Z<gC)|ifr`r7gwOcsGRiq?J_M|c~U<G-"
    "T*AHYaI(C1&{2MkJ)^fOulUa3_4iyCeiH~qnf(PVLPeU`WK+7hT>c3xc{^atmo#c({SZrohlo{g_6IB<aS$A`&c-"
    "k&TS%@r3(6NH;&thR^+^nyX-vIrk)n@j9+ftb9J9ore)IVSqrw$I`P^abt{%fiOZMkzxvqiB*w#(0oeMX(xx?1L7K!l1J>GhBxfL"
    "(DE7V@Q}TR_M5f1y1dv%jCapE_VXu9&?ShDyv>?VeX_pmPwMs9>|f#IG8YcDrxDB4)8uLEe8iA2S($TFc7rPB3jnL3L9$-"
    "qyy~X@-"
    "W)KL^DL>v(=5?1Q`TjrX$JxVRX!C68Nejg1@Qo!%7qV&jMwO?=Hhe_N6B`V4$H3=J}AUiL7q;0=OJ;HGyxtg3z=ct#)GM-"
    "hmhmfwBQlcN-LpiK)wJN1NP0?Q#*r`Nz>3tqI$yUX#$dlOgk3iM$0_c%4v1J|}FVS@lAsU8}xoSek1hLOG~tfGu2A41`sY(*UO&7"
    "bQ+1eOt05E0URk&V)!mR;(4g+UKNFo@hPDMSnUQ{WhKru7@M&%qZChm#>beki;W&JQTX(yh5!pTC2h8Uu34pU_Gs~lvI8oPy(emR"
    "U)nf{h0GaNf1X%z~d`NHfY27kR(v%BpgbR5X_d5IH8eE#*rw!0VXHLkcf*@+ebhk4q+4v8aP8D;}l^rGz>Ty%bSah<8w^An-"
    "!JpK$J9#m?{Cb)29>`|8L0(@LdqQPkKvJt)DJML6IL<Pz2v~p%+M>haf=UM`#0gLlAQ2huFy9a`!6U*nQ8tgr<X2X8xqL;2j2$<Q"
    "DueDARedM@22-"
    "slmMBZWm=t7pfMc+ch+D8)%d$G3)$^74QaGYpuK%@b#y&4%LY6W9X|M>ECrQe8eD;fsH``PeI$CAlvW^=aIr{KCKUpov4EVLKwMZ"
    ";7tRt5YSdSeP-"
    "B{?7~oepP`CY<o&j*E3Uhn+g5ML<D?EIyaJ9cTi<nPk0MN$9vBW7p+)~g4r>}LRQ5!lA7V$wXFvtzO(;5?XBy&!AJo3l(;Lz1Go="
    "A2JMT;3yeZ@4pc!6>o3q_1m=F#kFuvn?TZ(C8%Qpp&Lx*GLZd`os9-"
    "cY9yT3R0zZ^i_u>a+aK3A$fuWSjCr7&RF*pbLW8g;ub^)6=+g`d27E^#*9rJ6kvTAeuZn0a*kifAv*TMf&Vr56Z(I0J8x^9M4MF$"
    "oV=7>E~_!*P-c$yKz4ERC<JFp`CKg^M1A3RRY87rJW-"
    "1WWoYZ9V|kry4i?r;MD_fYO9mmwpiVOsbR|?C;knY{crP%M2a#0*}~~Id>*VITo_w$fD@4Z{2`8QI`D0G*-"
    "^M6a$saz~69eRaCBBnckWQgk>_>QX|F^nN{$Qo^oCtN0kKBbg7wyn#6pYQa%~4jvBNq^XeF@Hl+Cuo`0le!Kc!lOkeFzntPn>u0<"
    "VOP2Av;v65D)>rYP+Re09s*W`jmOY9<skZP#-te}9}5wOc~YA)7}w~fVwl|W&-"
    "!Z*QC?Rc3hUi^{y`S3T?Yqu(WSG`s%$XDi<_%%bjby?oG)ImAX!n43t%G&PLfw9C9qb&U`cPDfr{}G5_+yz^s&|=*GqRuGZZuB_>"
    "q3u}H7^2H@Xq;c_gg!!=SizOVA>6)4JxOd=h#xx7%skoeHPI?Rg}CrTpChP}<&6qn<!g(owEAEkS8A_MO33P#QUqMj9L=jvy12Rb"
    ";GrdkdOcr7Xl$g)H{*4|wT|sJNwzvRiClg|u+6V*u`8b%D75_Zk2=qMO9B?3eAEH+EeWW7;ZX%Fx0Jh;FRZJe)yD2TX8fH9_Ek_h"
    "ne)Rjz9+-"
    "4Kj7+qI$T_Xk{oO&WD(l41@=`IKG0P9T5j?65%o9Uvb0+tQ=iLs^uNLavBnW#sJK!3lA@<`(ipc}{{v7<0|XQR000O8001FSCyz~"
    "NV+H^K9T@-sAOHXWaA9L>WpXb;b#!laZeetEWo~3Hcx`MhbY*RDY+-a|-"
    "C1pK+DH)oe$xGi6*}FAlN=|_HL6m_6(LTF3JJobs3)XoF$1h(@4D-"
    "C2>tapYa3V_Ltd_G)%)h1XLfdG=XJsP@EC>U0c64iKWiKv95x8>Kuj2)oi$Q5wca&8xWE7Aq?{@Rd_s_)CkRP?ngnx*XktYykRlO"
    "NWd$NSU2!&W8zD{tN};fX#5BQu3&tm6k@UPAMh4sy3l3ZnP9r#Lbl1{`Ij_~`3M5KJ6=`U-"
    "gai$t2og&XK#~aAl);=S2vjOj1dS#qe<PZXLl%63<v`p6T6cUjo*ut@dqOA2Cx657+Xe|KpQUt$TR5aj(y+0*3qKICCgazm-"
    "^i^#T?EltW3E(uYTJeJ2W#UG&=7mrZMOuUvYGwn@bHc8E2>~+Dcb6TO5@vhr#N;EAY@R1TerSr*YG*^E(uPX$EoUwfQD-UCTXL>G"
    "Eoqf8B4S^=kqkWO+c2V8I;1s_S(nKcY0>%ujk<lmfYufDzk_+eXK!(N1W0?W%))YlZL@iu(U7SL&q+@O6ZV<;gH3kF;~eH9J@p+F"
    "}Eb3Zapd$)2AgRbQ|BVShnLvPC&Xxj-"
    "7vO;XeBY?$IGCpM7oNgJle^ciDFA?5m=WT~X+J>HFpheNXnP+x7cDN?q?!*UiGO#bSp|$2)DxRP9L?QMr7D;#+7rY@9B(hUs#5P*"
    "w0}SbZsEM3sBl92}#kiq#fZhmIk1^Frm=`Rc{-"
    "xmFAF3c1W>^^Pibd^a<%2bca+Ru(02r<omWsc2pc8S<|e2fk_f@#`;Q3pK+buV6;&+Fcr*c7!Fm%@ajK(_ZJs&yez=1>dC<(Ux04"
    "(F>~RGyH)~!?oMp=9On(H@lu=Yr+=SXBwv9-rZ%4cbf6;&ardq)=d?MSFUK6x+^;dqAF=`4|u-"
    "!)<;)P$hwF>7mM4rd&4~`h0NPXK{H)gbpXn&b5%A4RBU&eK>)Gx(vTJ<%^(<TmuVPY;}GEXo4p?S+$9+Gm?0~w84YqqIs2B!PKmp"
    "OY;>(?Rh>f|do`Taj;cuv0iz+dh8N7L7Z8VH86nHBH@oyx?k{;Tmx7D5l*(nKC8CJpQ{ah729iLsICIG-fS9N`5D95Q$03k0O@K`"
    "FJe1;n267oIm|(ygn@ZC5ly=MqHFqV<4&V_8Dnc3`KXtkz|BFBHx}#PqCAtF*S5kyHR*s6#(K*x8@jb`}u^&iJ!UOVMzyk}w%T>~"
    ")-BzUUUEN&_Z~7O+o{%GAPj%AanOj-ahp`Y?<WW+QQw7D$soKjlqPErzubZLg5QaZ`lHOQ?rr`qwWR}N&;bdX1H&F*OhFx94WOsh"
    "=;Hi_b;20jeHfP{^*MLRv58j~bQH^tg3Be~+PKZWucv|7FDj!0OA)i<N(^L0nIPQP<mi!rc@V%;XGgYD^X62Wp$8{B5zZHs=!I14"
    "}i4?C1i>9$Me{x84tVMdhxw`fI!QHLz^;a{_8Z<WaFt8UwmR}|787Y_1Yx=$}mGyIy(+er%19()0>YKG$BDW60;bH3<oJ%GXRhX6"
    ")(NfQPal_izV$8mj-!{SE>UYUhNYbOaiR@`!#rYkEwImh`j20b`S-"
    "Y~XMNf(;LxGm}2tlfM_XNh^lAJGfB_Y;I{Xf5^LcPZ@wyr_<GY*+8>-|W@OS^Aj{LF-0Vn<^S_>F?~jMvPViI1#Yg-"
    "hK88BgIo$?dUvejg&CD;Tl-dlnbc3hAvm1oy<khf9E4v<_`db7JW}NQQow^3zeM6Ll^UHS$5~E;?$4A&!)r22ZRkB*-"
    "7y`7aQYs`==gCM>8CP%st#urPfj=DB|O5*;)6&SJrP(uYI?W$ye!v&OXcPswq8_?j{aiB5*B0=iQgCZKyt6)?khZ+qVpwOK~ul&l"
    "jqDQ7cYNexheo_h9_!g$pqLpsKxDPkO(B)-"
    "eUo<PpuCUHoY+XK4^RQ6m+k;ZP*JOdxMIkm!iy{jD6$*nC%8S;{nl#6;sS<2m4UjuE^4W(G9cU@jzx5+m*=bpL!Bb$JC+iCW6pUh"
    "P&kt(d_VSXS1xUs1QtZcvGA*MiyB{2ll!W9ui%!&}(Yu0SrJhNvbp$;_!6eUM1n#JA_7wGy5)oe&o=m!2pq_Wq_-ohoq=C+NK_Kt"
    "Cmz54qC7yklKO9KQH000080000XP=>gV75M`I0O<+<02u%P0B~VrYh`jTcWG{9Z+CMoF)=Q1YjQ4VV{ElnZExE)5dL1E|KT7E@R!"
    "<-"
    "+oo8vWq_BZ*s!KE;=Fu_0)eK^77>b6`C`W#_TNW}qAg45;C+~2ST^su<MH7=M^=PBp@P3&zXDMB)iQ;7R&l#xLWfa+Vq2kF!+HD<"
    "prut5!3`xVW(vC)QCW@)q6<c)s>Z=1iSRWl&7|<~bC`@KqtnLpw|}`W_j&zlO%x*wj*t**q!q*%6fPNJiX=>JTv!)G8^y$`=S3^4"
    "+d%O730p2u`LP_A#B$@t-uGN{rk^s+{=}?Y92Mfj>FK)<y)Y|_+PH+Z-bj^q0zoTt#~=#L3|ss47-"
    "jJrv8+ZVNQu3q_L25UC5luP$x9}ZUO1*@Mhm1*+LlML=^c)yzQj_h?Xl#2Kl%8!7eZQ7S(D|i0I6}oj+$3*n4v{>JVU=UKj*b$pC"
    "*H4b^Nl|WpC;Zwh>Aa1Tl1^CXj5H$mK?7lS$*bkkVvMK_wA6#OE9y67u7QF!NJ<C67C_AAr{5);1}1Ei0O5OU6;dq5Z+-"
    "J?bgzvGL$!fxP39Tu*1SY<_ujI}3qbhE_02-2Sv-Zau0D2q!`4KIh<P_NIC>qSX43whBEIg{L{wNUg%mFS~{Yx$MlQDi0z>^9ltj"
    "Vtn6eo8Q*9T3jU0nYZh#l)2wJ-"
    "v@lmdMyQ#+_BiDF@|pos<V!^DMGC}WVZ$N+u&hOh*hR=#k4`!g(GZ9xUOdmB72eCo&G$otE3jLYYLrcM{nlKpA%DaamA>TS}x6fD"
    "A$@4U0CD(h=Xc%;7V>>k1vq(5k4afzsQ-Az6xP@(IC@gj%N6qn*xS2w`91VUlDPZrd(3O3#m<-"
    "&YegY#WbCAE;qLV1y$S1I5LKJgj<B~YBqj={}RfYB29lLn$d2QxSBfWv4*jM$q9^?FwUVmdw({8F@=Fw0o+}|f@lO*k`;O-"
    "R2&Ts(&Ug9!%B1{M_S&U1YPJSR(Z-"
    "QLiYvP+S=NV&y`fBy|uB{T5Ybo^DR@|gJS>c*T~M~aZTrXsg@d(N7cgKoo5HA!=r8wZW9nV_}Fj|?D0T*Ay_mut#e@+&qIF<T~ya"
    "CG5j9w8|tXlP9MD^K&9lG`5TA3*|bVCi5D0qI1|3eAL0!qpy+ZHN}*s2pNkWMTrQJ0JJhw)*&6H0bM@^qFx#dA2fzOQ`N~z`{Ets"
    "J_tWdkG~MYZO&bNlmzy-"
    "buu7pYci~D@+qhgwF>s>syfi1&ERsIFR7$F8sGGS{lrVgIA%$VWVk@<%i2o}uCnGuacZ<({G%9IuGI*JuIQ_-hZkjZm5n&2cX&R5"
    "9(R0ZMZ@vM#Z9pA33_nSKrv5uIA*aXv{qi4BO9KQH000080000XP>M1JI{OF!06QN501f~E08(Laa8_+hVPY<Db8RubS#59QHWL0"
    "GApe07j9VM1gzW(>dI1cq<2bu1;@Ggf>EW_Lp-6PhMiO0;a+15|zuyc=NtCQO?p^M*z-A-O3?I(>%!X9?p%N@sQ=U-"
    "bUsE9&&&g$^s8q*Cy@?Q9jA8{Z=Yp=Npm|Kmka(fu8}In&_-Iw+`ZM_qvKG;1a~a)TM$f!Z<X^`}1fH95mZVgjvOHn=eSdIkUT-"
    "21W&Ilo$LIIAJz!gKu2A;b$u|^qoxwYAfQKM`Pngd)7qeg<srBv22^@J|q$&Q^F9i(jp&J<&Qt^!6{YGPT`^kdAN1xMphDLf#GLG"
    "UkZIS%US?=Rm7K#@mk>@Z8n$TRaD3yDdY9fdAa{>CU`QK#yc8?5x{U(T0_LQZL$crqxr;<2Nhe)Q09IgeGMXKa}E@6mVwjysF)y)"
    "P(4o|3}docZe9%+aiwk7AOeCsHML=MwDiXW&rgz4KxliD8veWE*J=4k<#<RN1GjiGg9%w(Lf?2T(18QhSTKU-kFaH&9titZD%1|n"
    "Y~Rq&hSxn+MjK6+^c?=ONWs>AnZpgJgWYalmsd_ffz{b`gZk>cVRLrRH)4sLrF`KC}a9fsc>%2cHVyo<}la&_A~qZ_#4ko;sm)F}"
    "dxK{&vdaFa4+6ajzhms*seV=L0Pv;*QKhAaB$UnrUp{rB>DL&+HvfE%&-=UhPUv)Z*M{Xu4h@~<EXRf^R>oI3-"
    "}nCDw6)ROyJyS~A1uki;7A#(zWLV;GiK|aZ2j+!T5m*+pVO*WDeWNMpz0i@!36vtG`gKSr63^n2B;3)mi8bp?XEp#fsp2GQc_9r1"
    "r0blxzKv@npYG_Wa1%D)-2I60nIe(-gT+=iq+LH-ri{LR33Mxudngm`$VG0!Nh%*4t!CN4p>g?*A#F2{Ed*Cps50A8h*j-"
    "8i2hhN4$?kI>ev$Zr=K&@%a*;DksqCL7B6J-JHu8HyQ@VvnO1=YTnrmi)g${Lg2k{PK1JdjFehns1F&GymPC+u{*uiU&SC-"
    "9o1$gJ;nVOP3>?qTI$z6(RyT%erjqyt(CTM}}^aV{r>I$Vzu;K;iDpKSFsOc49AKtLSiV3M&{?l{L8A9pXa0rdDE{S9>bSEJ=B77"
    "zh?G0omuw4dkgHZv^M5IkR4{QG0gRZ_}=yMYMV+%J*PWE5Fc{M>*A#(SIZ5OiX<y`Pgt16^%A!w+5<1jzkpNq9Trk(>=@NLii%}K"
    "#ffj|&8YG6ghG8$aq3l6ZvmO%st(@4lQsP5#%6|v-};d0S$i|xn`RwD<<pDVHCMwAh5(GAMXv0^!-"
    "qlWYY#Qp=`p9@MmWwxz@MFp)g2F)_iEj@)00C#xL8e1iT1>JDT@FNEDpD(wNS)p)MMb8ybl6+=rL09d{E8t*|*N6U*r(0@ct_f!l"
    ")Ft>&l-d@io&4W><l>>(`?Oi0RkzCbMFq)*S?|u+<3Is{A-"
    "Bv6nsK<Txyb@OSJD!`!L_%Db_lV&7StQuhW{_*o<X`vc@7Nz?**ff)FE~I>qsOi%O9k*k4EHVyvtFzoc#S_Ii8(Oh!5N!yRzAs7i"
    "priw>hFx1*vuE<Sa+Nag~NlgVi5f?Z5yPKj<P<;ZCT6xr#LW>`=s=sD*J!sL+yvHW2m-"
    "60nh9Wm_lXzCfXu)RhbEo?1(Akx%{l0$Qc1^f9?h0ItWu1pdLHI}rGWKE-"
    "K~Q0%`U<U}%fhuhG+$f!W=*LKhdIxd3GiVKSR>;v8u>erTP4~L$|Tx#b;L{<j-$;pMpK%0qQ)-"
    "WK1Fx1edAT0ePwhrl@tJNlXA>vkO8BcU&w3rg8hme-F%QrZ+$L!%m<aMv&UjkwgrH0oc(Vuj-xunr*=kE9%o|*bxQ-"
    "*_nu#>9XXUsRx_MlFrXO0>gIx!fU0*%Y=Q$Pb($F&<t=rzuEj%$HvIN+->A0-"
    "eZqjv}e+zlKW1}zK;TdmxX)yZcsB>Fq~eg{%ZsvnaAhO!`sN;~uxqxqb`7=?{^^@(N?ONX9-"
    "hQQxuej43<N_iZmIH!9MNLj|5WSEgk3Q*Qp^>!Wq5Dj)}5&FtzHZdRq?{(u=&h{Uf4Q9X%&c)7&>nOkPG~G+H#_g#arvx;clP{Ce"
    "*?&{v+RD&E??jZx>sDXhLSzfJ6;Rf1WPeXMc%%`%Q*nFHoMH#o!X@a|hh`E&7F9C{mV)W|U$bn@zE{WjZmQK@`YT)>r*@isyPhn<"
    "i`kXeWCq4&-"
    "f^X3b+D@iv)^bO34QTniKwc&#QPY)AFmqi%AJAef@nYDVCe0cTPqozqiWTflY~>VE5MS5rg!A;Xnfy}*);k3aPtgHpK$iYCfe&~s"
    "Et??l<Rnx!0ON0^OjdD4;wny?H~)+(O-"
    "Y~5y`Y+&LL@jiR7BJH3d03z2`9ZtuqpS83E5AKtgAMt1A^WQ8m0~+gCPmj&0Fu&{_Bj#wX8-"
    "^42;sVrENGFOp0R{@+YZ*V8MYI(%9>U@g$A|Gl%mT*7n-xeEqeo+sE<{_W$(_B@r)DACO-"
    "%+Y7ynaBg}*jE)_@yB44B$m71l4c`2;f?myuD9?Cd7~L=P1Y@9Y=!1wXn*&Onut{wq?mfa;aqojW7m{_k#G3}t#*xmDZV<_4`abL"
    ">J;kY1Nsonw<qJ-bpCZYSzL{#6Y!?DmxAR}ZcnUmw}|a*4e`+qY>Cl>ZCg}pp@z9{G;4Rlp^Aj^!<5nu-"
    "q;xahmOhPagD2@{;ti5pQ_p|Do3#y%vreFK!Jp&6WJXcmf_43CC@kvz~p1>_klb@Y~viz@<(ZYV!CTarPYPq9zsv@e+tHGxl!bG("
    "_e?mHnVF@Tv<0g^zGSO+k2Zes)BtNnEzbCGVRS)D{rT>LC5PjbO{bO!}ik73U7mOJOCf7=UvH8&;8=Sw|XHy#*<t1?1yH}+q<%8s"
    "JKkalPA4So${ne>6B)7SRBqvulQt5?CorpJ!?d-`M*om>sS5<qx$~JYP|ZsZ|_+Vy|R9*vAtGmDvGw-LtKFK{TonA0|XQR000O80"
    "01FS#Zj3=?*;$>%MAbk2><{9Qbj>TO+_wkWQ|wdZrjWey$_Ig7$61O3L+Z^anL5{g>0vefVdWH*X@M?b44zxt;k(|`y)j~F8UgMy"
    "*^3L?5=1fDA3+mB=>Lj%sFSqZ|H8ZTG3yXZp_}%*%>|Fkd?g@PEs${uV1}>^{`Qnp9w#HBWbj1r+V4RW}4XvFR3*)jvqI>utI6)<"
    "v{!+`d-?SmY%j!j*jq-O>HMhI48X$qp7<3_;e@6@p1Sn*43QWLG=x$QjKHuX_RX|b+7z}R-"
    ")cYOF}pF<uFQHJkH}wZ6$)@#f@^Kabn#|JhrX0QrAj%{CyjPmOE(=<Z7vfRi>l|Tp}J2XW-Uq7=q^wK9LJ`EuCvaPuSf9E*xPo6-"
    "ap5%xS*?Hq;9IZKhExJ+Q!s7_x}N0pIJ5thb|4+SB@gJz5cZUoz-#-"
    "q5X<g;#^5jln^{D2zOE7c{lj3=<qHvzPXMBLV1nd6vR=wN<0XxxWNN>F6(uOH$s+zMT`UiL1CHT%=mkQZ^jCXquGcI#|HuNz}Co`"
    "1OWnv*UtAGbpW`x569iX0!P*!H!0y`I<Q?XXV*>`TjIFH1?rWnn%iW3cA58WF5K2RdjCz&c9K$HO{pD-"
    "~ap<b~H9ZPq+7%SIe7gdRLx*pb-a%E>i#(J01*7uBE5@FN@;c`G=pGaJ5>jmIcyp4<nLA9fQN;4eqK$ACa%BYGgzmBl`MP`Q(l1-"
    "P3L;pn<2QRy<SvLlzTL%h8?1b-aApMgX<kPj~LD2_p@1So5xGjBs;2-"
    "fX2tl3FX>W}Z?^d#h5k!C|$l&4@^6Go<}i*K#(a+8|gRgjYtFwD9@7Z=Q^86gUhnt4<ey`8QxUb3oZBRwT*#-"
    "_9rIh~UkDeQM<HKsM-<e2}}RjT8-"
    "7;(pY)K?t8n8_cnoY9p~muyN$mW60nPN5;BIv^w(ng4LW3z!ZZpS!Bs!Bz@kAKHZ5fkqzvl2F|czDE{!aXvE>v06y~+I1vJq)5?<"
    "W5|;6lC}H7=!}nR_AKnr+a-ZS^Tv$s6=<l-jE}aJ-"
    ">Y0>&1H<|Kd7S;<Xz?rM4E>RQVh6YvX^{h6I>X$cVgb__{mT`<Dwqx5{ipSRmixH=0--NCoU|PKtOSV8hnDe)KizKxIG#SH=ZS<2"
    "=<@!SoC&s$7*3-"
    "4wVTBKS$DkxSl>RpKgIJT6YaiNdYdfeDA0(Q3j?51yvT;ACAfihFjp5fXJrjCCOTy?(nh#V+A7;aw0Gu=qicywq%+^m>0Z|Cju*!"
    "GIqj77LG<*nx?w%TG=%pO&e2eBz+9Nti5(@$W7_1|gxg(TP;<~?P&GY%x%%6Yk!+=r2qzT(e=J}J-"
    "DdeeKvXxvTlMV+7l?o*JEtKIM|pkZvF~)BOAUReO9Ngq&%g6PQ52N_@@o~zT;bE7vSLmY5UmeNyjB2db?_Ub=d3}ze+g^4{JPAWj"
    "8+~CaKn2opl*DNzTlGA^svb0FxBZMuf(LFdC9#PUQl|O<@bv1pk;lHOv@oSE;<8>-D#fEZei>!=)?Q1tlTLRzz@-"
    "#_7QnXldCAAgrV%XSXZEOUk(i_MO8|@t8$`2W(N}^KnO;EXM8_Lr6cka=TA)O6zVLB4i{*ypqzX84bV=K*c-"
    "d$<GhuU%Ua!shTns(%`hm>Oy_e^6D^atK?dNooi^;SErNE5;;FP`ON9xgW2%fDbEQfd<SwEx8vcu0DQon=aVR|o??8TORjXtY(hK"
    "k@n0e|S+|SuWe2p9#dR-%_1D8<j72W@&Et_Yh#`1u6;Nf9K@7}&m&{V%e0qFgvidwmY;Cr98PB-gKms%SxS4i_qEr03Yo@`oHl}N"
    "a0LaGZdJr4>5c-4UBiQPqHA!is4q#C5IDP}p*RqCkl4n1v8I;z}Cah)3DAqtx3LNGvCB-"
    "U7LewZg(A1!RB<o@ITR{JHGX@9KsRNQinctDA`LV2LG_ml3g3<$vz=wL{(j3{^7FvnI-FeAsX?qNqGYHg9*G~)iO;3=4yWxR-"
    ">xm>Ht$+EJkMB<1pW)!3iacLs^QByS#h+w*@5KoPHR87Rd;)2iX<G@oKa8LVWH_yA_8CX2WujP2CVpT@-"
    "P@qGu*}+&AiKJDwsK;TM=*q1;F{Ir5J0ub}u8vJY=42Eix*G5)HbL`T{HN9^T{ri0{LcUyrBRI%<%xBX>wUfDR!cXT*gjazP_q>*"
    "uaYh+oalp_0$|EHYJ!cWf(K<>4Spv%XTH=dVz?{&QL2D3@{(?28-"
    "#lr)XE6I$SGrWRPj1Y>0|kPM!DwqSp1&3N8vYifg{uN{i@WYBx6JEWUm)?tzbN`H+BG??Sh4RBvShyP)h>@6aWAK2mk;8Ay5}Y6f"
    "-3R008U>000~S002^DXK8bEWpXW2VQ_F(ZA@WeQe|^>ZDlTSb1|J&TTkOS6n?MN|6o~tNVGVDw-wSz!<1#{ER>1>^FS*w$!Rg0*c"
    "sbtr(*f<d+c1A6n0m;d8llk`**%`dOyz74D1&nQz2JDxEKx!u6Z5|2L!)+V>P}nMi>0)S}99D5qf$&zve}8m*X2f*wed)LK$I|-"
    "a7TZ^nS4z#R*8Rg+fQ41G>~;p6LOhg$5yw<yi))yKB&;bceE7X`TWNTUQ%llV=wwS8Es!!r@>zh{3WLV<h%cr9jvnXd{#)7u<re!"
    "@=k`t(87WEI!UOEJ1@zz!ei)RnXyJk{3!_hSp^UB>1L;WHWA`$!HeGi57+R)zh}{s4)2v4GB9_Isuo%2s6GyuigwjpZ`9-"
    "J)XyEX*XQM{8A)Z8NAKEBi3qT=HpUh8n(`LeqEVkGNU!mN|^H8XV`|k22<uvE|w&y>kr9mg-dm16ASrFs{*v$lDdL!Ud(&#1YjLx"
    "NGvi;DBF&ev_h6pxz=DyEr)|QSEY;1Bto&*={AwQcdX!kauvDYi{s<3V9&}dbGP8{L5`w%6wxsBA$_q8Yof6#r6ml0ki#~jeb#D2"
    "=!qp6aAS#*K<+L{!zWEl!#QEFm>;FkkVdpFXq54-"
    "DqWtK9CKhJ)ECtoYgpgVzv}WNb$!vk9qje+jlCYdQNl1$=i(GO=V_61tYwSe<z<?(^Yc7626;^Gzm_6JFs86^ryz`ORO|;Npi>$~"
    "arsouOK^BVehsUbr<io&K*i7<;F<&}Ut#AMDw=tfqT^8^3dn?nzD*zOiCn8cfVC`})iy}*Bj*D_v<;^_PI@U(uN1u)C7ns8R{v(u"
    "WEP>Wk5ad2Y}RPD+Y;;rJrH`}bP|>4Tzc#awZW-"
    "*hAfNVC!#%7NcttR*B#|VTF@LRy~cYrZL!^=@LZ%RNaXxaNJ_s8R3?%w`LZpzF@%y|Dn?Ou=6pTU7QsjCZ#^VSB=C+Is8b(NrQ=|"
    "43Q(>8;vB}EqEVrP!JaQqIn?lt^_Fc@oLzHql8YL9e6QQ^NU7sFvdwRY54VC}V&qS9Ra!R1`l^lk-<QdqJCdeT-JtIGW?KN+k)V$"
    "H5kI<_IR3**;7D+fKQ0udQ{3R`;&Z$FoZLN~*jt-86*q-"
    "9A_tr^e3`0EXUG%{Yda6@?)yY4h%4#1=37VF7Uu4|CbaUl6_rNQjE;x8DSr8U*TPnl_YEfpF_J}Tuby5I1k$g$!YKG?@T)ac&0hG"
    "=K7)6_y$7KWf%|IOw{q$RfbQfDhSGH88!qtQWA(69`oV~md=Rpuj)Y3Um^vhelfKIxZ`w9}^x1T9i1r%2GrKKP{y)riGg&9oAJUy"
    "-19uBj`-"
    "jjbUQe%SG@6HwlO7$qWZ30n%B+d<9vuH)O+FOAh0P#!IM_pBIQR=tO9KQH000080000XP@tzlJR}4F0GtT`01^NI090jjbS+Y0aB"
    "x;_OkrX!aC0%0R^e~zHW2@g#Q$JLkzTSjd3(}6Ayq14v}H;Gk+zydQRO-Z_%*RJ+j(uZz5jjZB!<9X+7PIT&v*B`yWib)IV!Ro%r"
    "9JITx^1H)$f&5(IV*g2!58@C_G>J34K{eX~-"
    "q<ejPk5XjwiMc;;QWdvDyZ?aE)k9~D<Hl48v_m4fV6YSZt9{a(M9f{9YJ$IP9~fJBd=G?#)T)PTL@kCl>Y$P6CN6|6ylU|?OQMwV"
    "W`Hz`V~OoZB14kY+ZauLm`*%E)ArcCkD)EK=TytvfG7cV5ywNwl&1|O^sjYg;N7R_G10yAVJ^BiioI=%q`2r*8$HZFQp)3tf4cY{"
    "%kwmi=!1`2Y@e{{`r1B(2B?!R<&fBe771!}LQ0?M`|Xw48Vh_e`yKb!RXM!tfu=zLM-"
    "d3%V3)G&7Ob|lL?D(D6Z5GEd0Mi$h@9w$_6Dm;(pR#B}6gZcphf%6_;qmd~s;DRi%LaWxXd+T@%$zNnvnP|H6x{qXkt&ZkEtBt4*"
    "ps7_n%(B4qcMz=ma6tU7o%jy4M(CjzHu~TDz3;Z(MtwMw%l9H*`BdmPP&Ou4ODPN{;$P@gQuYe!$!4k&)ZpzbMq4qKu*{LWmS79|"
    ")@EHGJdG-F$g$s10e@2`ZAzem4xl=+d-{??cx=n&V5b^*m3KkBN{NAHTPUcG3eJ?&a&00ei-AMwlHpUv5W4N&uDcX0>r-"
    "TS4pZ#NV4r&L^XF=y!59?k<yA?wzWgNR3#1<!!~V2FF?uScz|`UM1M+3qIMMi;NJjHB?`~uq2H2dnc=?(Hk-"
    "*eD;OA*^wkQLVTc^Z@zU82(V%rbGHL~s-"
    "&3P7g*+Lk_3AXE~|L6o+_#BVl8I*Mkb!k}h&*wrLisMDq%(^7Y$t<>y*j>mz+fMc^IM2Q~e!_2S#!eJ347+yk;oTfj`N(NQ&VBoB"
    "rF^xGchwf$TMXy(=gBm^A12B3VmzNcKP(bgrxVh}`1-"
    "W;alA+;v*~H!boQJKAEu*QoaEuIqPEsY!PwFlbun<NY~USJHP(!l&_EB*v!RnETjqjmjRYpOT6{bj{G5Ks%H_`P4BQw=a~8RM=N4"
    "bTR|7q{-gbDp6AtrUr?~YJ+l#3|&Rh_8bW`El8=(=b8K?PPFs}#B{(Yud#*58i;JYRX?$Jz39qae-"
    "+COr%$4<70iLC7?+$U?$7;(vJ6W00DnW*+N)Y$q>`ffi;P><N=*aWT0VN)GrIoUdgMXIyjs*LJJjy8t;v<uN}m3-"
    "S>A<<WCBeEQeZ(K=X7aWoYr*OgrxRzX&npGONo~$SH>Z&zmt5fNH)-"
    "LVj$LKPzk=M&GOWS2`<!%o*$eLRdN99}OoZY)WH|MtgEqk)Y`tn7}{Oo^B2=#AJO928D02BZK00;m803lGDQt$>S0ssKL0{{RM00"
    "000000000001_0RR9107GnLVR9`}VQ_F(ZA@WeE^u=(P)h*<6aW+e000O8001FS8<J?_i~|4wPzL}2761SM0000000000qybq100"
    "2j2bS+Y0aBx>?Ze(wFb4hb=E^u=(P)h*<6aW+e000O8001FSSUr5=;0gc$#vT9w7ytkO0000000000qyZTQ002pDX>@5}Y-"
    "xIBEmC1{a8_+hVPY<Db1_g$0Rj{N6aWAK2mk;8AyAKHmrUFe001yV000~S0000000000005)`FA)F$Np5y;Yh^7`VQ_F(ZAor(bY"
    "X04RAqB?E^u=(P)h*<6aW+e000O8001FSw!R#dR0;q9$s+&&8~^|S0000000000qya@F002pDc5iECEmC1{a8_+hVPa5eaAj<1Ze"
    "=cTb1_g$0Rj{N6aWAK2mk;8AyDp@^?e8f004>y000{R0000000000005)`(=Gr2Np5y;Yh^7`VQ_F(ZB%7*bWLG&a%p%jaC0$GO9"
    "28D02BZK00;m803lHL<laUz3;+P#Bme*v00000000000001_0TeO-"
    "08V9hEmC1{a6(~oWl3#eXJsyMb1_g$0Rj{N6aWAK2mk;8Ay6leO=x2V0012s001BW0000000000005)`dOiREaA9L>WpXb;b#!la"
    "ZeetEWo~3Hcx`MhbY*RDY+-"
    "a|P)h*<6aW+e000O8001FShPaOv`2zp|=?VY<82|tP0000000000qyZa6003}dV{2t{FL!BfWN&wKEio}JaBFfdXk%<pO928D02B"
    "ZK00;m803lF{G6p*P2mk;(9{>Oj00000000000001_0ZT~$08(Laa8_+hVPY<Db8RtDO928D02BZK00;m803lGtQJF;V1^@ud4FC"
    "WM00000000000001_0di6R08&LkL`_95ZDdeO0Rj{N6aWAK2mk;8Ay5}Y6f-"
    "3R008U>000~S0000000000005)`h*<ytQe|gpb97~LEmC1{a8_+hVPaBcb9HTHE^u=(P)h*<6aW+e000O8001FSpr=7RBm@8eoCy"
    "E`5&!@I0000000000qygt$002~Fb960IVQ_F(ZA@WeE^u=(P)h{{000004FC-QeFFdhJ7NF;000"
)


class WindowsVmLabAgent(BasicAgent):
    ACTIONS = {
        "setup",
        "download_iso",
        "build_base",
        "test",
        "full",
        "cleanup",
        "status",
    }
    SCENARIOS = {"fresh", "preinstalled", "rerun", "upgrade"}
    RUN_ID_PATTERN = re.compile(r"^[A-Za-z0-9-]+$")

    def __init__(self):
        self.name = "WindowsVmInstallLab"
        self.metadata = {
            "name": self.name,
            "description": (
                "Operates the local Hyper-V Windows 11 release lab for end-to-end "
                "RAPP Brainstem installer testing. Use full to provision or refresh "
                "the lab and run all release scenarios asynchronously. Use status "
                "with the returned run_id to monitor it. Actions are allowlisted and "
                "cannot execute arbitrary PowerShell."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": sorted(self.ACTIONS),
                        "description": "Lab operation to start or inspect.",
                    },
                    "run_id": {
                        "type": "string",
                        "description": "Run ID returned by a prior operation. Used by status.",
                    },
                    "scenarios": {
                        "type": "array",
                        "items": {"type": "string", "enum": sorted(self.SCENARIOS)},
                        "description": "Optional scenario subset for test or full.",
                    },
                    "older_than_days": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 365,
                        "description": "Retention threshold for cleanup. Default 14.",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    @property
    def repository_root(self):
        configured = os.environ.get("RAPP_VM_LAB_REPOSITORY_ROOT", "").strip()
        if configured:
            return Path(configured).expanduser().resolve()
        for parent in Path(__file__).resolve().parents:
            if (parent / ".git").exists():
                return parent
        return Path(__file__).resolve().parents[1]

    @property
    def lab_root(self):
        configured = os.environ.get("RAPP_VM_LAB_ROOT", "").strip()
        if configured:
            return Path(configured).expanduser()
        if Path("D:/").exists():
            return Path("D:/RappVmLab")
        local_data = os.environ.get("LOCALAPPDATA", "").strip()
        return Path(local_data).expanduser() / "RappVmLab" if local_data else (
            Path.home() / "RappVmLab"
        )

    @property
    def runs_root(self):
        return self.lab_root / "agent-runs"

    def _ensure_pipeline(self):
        tools_root = (
            self.lab_root
            / "agent-tools"
            / _VM_LAB_BUNDLE_SHA256[:12]
        )
        pipeline = tools_root / "Invoke-RappVmLabPipeline.ps1"
        if pipeline.is_file():
            return pipeline

        try:
            archive_bytes = base64.b85decode(_VM_LAB_BUNDLE_B85)
        except (ValueError, TypeError) as exc:
            raise RuntimeError("The embedded VM lab toolkit is invalid.") from exc
        actual_hash = hashlib.sha256(archive_bytes).hexdigest()
        if actual_hash != _VM_LAB_BUNDLE_SHA256:
            raise RuntimeError("The embedded VM lab toolkit failed verification.")

        try:
            with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
                for member in archive.infolist():
                    relative = PurePosixPath(member.filename)
                    if relative.is_absolute() or ".." in relative.parts:
                        raise RuntimeError(
                            "The embedded VM lab toolkit contains an unsafe path."
                        )
                    destination = tools_root.joinpath(*relative.parts)
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    temporary = destination.with_name(
                        f".{destination.name}.{uuid.uuid4().hex}.tmp"
                    )
                    try:
                        temporary.write_bytes(archive.read(member))
                        os.replace(temporary, destination)
                    finally:
                        temporary.unlink(missing_ok=True)
        except (OSError, zipfile.BadZipFile) as exc:
            raise RuntimeError(
                f"Could not install the embedded VM lab toolkit: {exc}"
            ) from exc

        if not pipeline.is_file():
            raise RuntimeError("The embedded VM lab pipeline is missing.")
        return pipeline

    def perform(self, **kwargs):
        if os.name != "nt":
            return self._response("error", message="The Windows VM lab requires Windows.")

        action = str(kwargs.get("action", "")).strip().lower()
        if action not in self.ACTIONS:
            return self._response("error", message=f"Unsupported action: {action!r}.")

        if action == "status":
            return self._status(kwargs.get("run_id"))

        scenarios = kwargs.get("scenarios") or sorted(self.SCENARIOS)
        if not isinstance(scenarios, list):
            return self._response("error", message="scenarios must be an array.")
        scenarios = [str(item).strip().lower() for item in scenarios]
        invalid = sorted(set(scenarios) - self.SCENARIOS)
        if invalid:
            return self._response("error", message=f"Unsupported scenarios: {invalid}.")
        if not scenarios:
            return self._response("error", message="At least one scenario is required.")

        try:
            older_than_days = int(kwargs.get("older_than_days", 14))
        except (TypeError, ValueError):
            return self._response("error", message="older_than_days must be an integer.")
        if not 1 <= older_than_days <= 365:
            return self._response("error", message="older_than_days must be from 1 to 365.")

        active = self._active_run()
        if active:
            return self._response(
                "busy",
                message="A VM lab operation is already running.",
                run=active,
            )

        try:
            pipeline = self._ensure_pipeline()
        except RuntimeError as exc:
            return self._response("error", message=str(exc))

        run_id = f"{datetime.now(timezone.utc):%Y%m%d-%H%M%S}-{uuid.uuid4().hex[:8]}"
        run_directory = self.runs_root / run_id
        run_directory.mkdir(parents=True, exist_ok=False)
        state_path = run_directory / "state.json"
        pipeline_log = run_directory / "pipeline.log"
        launcher_log = run_directory / "launcher.log"
        initial_state = {
            "RunId": run_id,
            "Action": action,
            "Status": "queued",
            "ProcessId": None,
            "StartedAtUtc": datetime.now(timezone.utc).isoformat(),
            "UpdatedAtUtc": datetime.now(timezone.utc).isoformat(),
            "Repository": str(self.repository_root),
            "LabRoot": str(self.lab_root),
            "Scenarios": scenarios,
            "LogPath": str(pipeline_log),
            "Result": None,
            "Error": None,
        }
        state_path.write_text(json.dumps(initial_state, indent=2), encoding="utf-8")

        command = [
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(pipeline),
            "-Action",
            action,
            "-LabRoot",
            str(self.lab_root),
            "-RepositoryRoot",
            str(self.repository_root),
            "-ScenarioCsv",
            ",".join(scenarios),
            "-OlderThanDays",
            str(older_than_days),
            "-RunId",
            run_id,
            "-StatePath",
            str(state_path),
            "-LogPath",
            str(pipeline_log),
        ]
        creation_flags = (
            subprocess.CREATE_NEW_PROCESS_GROUP
            | subprocess.CREATE_NO_WINDOW
        )
        try:
            with launcher_log.open("ab") as output:
                process = subprocess.Popen(
                    command,
                    cwd=self.repository_root,
                    stdin=subprocess.DEVNULL,
                    stdout=output,
                    stderr=subprocess.STDOUT,
                    creationflags=creation_flags,
                    close_fds=True,
                )
        except OSError as exc:
            initial_state["Status"] = "failed"
            initial_state["Error"] = {"Message": str(exc)}
            initial_state["UpdatedAtUtc"] = datetime.now(timezone.utc).isoformat()
            state_path.write_text(json.dumps(initial_state, indent=2), encoding="utf-8")
            return self._response("error", message=str(exc), run_id=run_id)

        return self._response(
            "started",
            run_id=run_id,
            process_id=process.pid,
            action=action,
            scenarios=scenarios,
            note=(
                "The first setup or full run can show one Windows UAC consent prompt. "
                "Use status with this run_id for progress."
            ),
        )

    def _status(self, run_id):
        if run_id:
            run_id = str(run_id).strip()
            if not self.RUN_ID_PATTERN.fullmatch(run_id):
                return self._response("error", message="Invalid run_id.")
            run_directory = self.runs_root / run_id
        else:
            if not self.runs_root.is_dir():
                return self._response("not_configured", message="No VM lab runs exist yet.")
            directories = sorted(
                (item for item in self.runs_root.iterdir() if item.is_dir()),
                key=lambda item: item.stat().st_mtime,
                reverse=True,
            )
            if not directories:
                return self._response("not_configured", message="No VM lab runs exist yet.")
            run_directory = directories[0]

        state_path = run_directory / "state.json"
        if not state_path.is_file():
            return self._response("error", message=f"Run state is missing: {run_directory.name}")
        try:
            state = json.loads(state_path.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError) as exc:
            return self._response("error", message=f"Could not read run state: {exc}")

        status = str(state.get("Status", "unknown"))
        process_id = state.get("ProcessId")
        if status in {"queued", "running", "waiting_for_uac"} and process_id:
            state["ProcessAlive"] = self._process_alive(int(process_id))

        log_path = Path(state.get("LogPath") or run_directory / "pipeline.log")
        if log_path.is_file():
            try:
                state["LogTail"] = log_path.read_text(
                    encoding="utf-8-sig", errors="replace"
                )[-4000:]
            except OSError:
                pass
        return self._response("success", run=state)

    def _active_run(self):
        if not self.runs_root.is_dir():
            return None
        for state_path in sorted(
            self.runs_root.glob("*/state.json"),
            key=lambda item: item.stat().st_mtime,
            reverse=True,
        ):
            try:
                state = json.loads(state_path.read_text(encoding="utf-8-sig"))
            except (OSError, json.JSONDecodeError):
                continue
            if state.get("Status") not in {
                "queued",
                "running",
                "waiting_for_uac",
                "waiting_for_sign_in",
            }:
                continue
            process_id = state.get("ProcessId")
            if process_id is None:
                if state.get("Status") == "waiting_for_sign_in":
                    return {
                        "run_id": state.get("RunId"),
                        "action": state.get("Action"),
                        "status": state.get("Status"),
                    }
                updated = state.get("UpdatedAtUtc")
                try:
                    updated_at = datetime.fromisoformat(str(updated).replace("Z", "+00:00"))
                except (TypeError, ValueError):
                    updated_at = None
                if updated_at and (datetime.now(timezone.utc) - updated_at).total_seconds() > 300:
                    continue
                return {
                    "run_id": state.get("RunId"),
                    "action": state.get("Action"),
                    "status": state.get("Status"),
                }
            if self._process_alive(int(process_id)):
                return {
                    "run_id": state.get("RunId"),
                    "action": state.get("Action"),
                    "status": state.get("Status"),
                }
        return None

    @staticmethod
    def _process_alive(process_id):
        process_query_limited_information = 0x1000
        handle = ctypes.windll.kernel32.OpenProcess(
            process_query_limited_information, False, process_id
        )
        if not handle:
            return False
        ctypes.windll.kernel32.CloseHandle(handle)
        return True

    @staticmethod
    def _response(status, **values):
        return json.dumps({"status": status, **values}, default=str)


if __name__ == "__main__":
    print(WindowsVmLabAgent().perform())
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
