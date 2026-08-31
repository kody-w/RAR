---
name: "rar-kody-w-windows-vm-install-lab"
description: "Runs an allowlisted Hyper-V Windows 11 lab for repeatable RAPP installer release testing with an embedded, hash-verified toolkit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/windows_vm_install_lab_agent", "rar_sha256": "cb3249f0118aa4edf62f99daa353c1fa9ad50c79684832158351cdf81b9ca1bb", "source_kind": "rar-agent", "source_commit": "078c9f76011af965f40983af7f225debec8e76b8", "author": "RAPP Community", "tags": ["windows", "hyper-v", "installer", "testing", "automation"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `windows_vm_install_lab_agent.py` and embedded as the fenced Python below (sha256 cb3249f0118aa4ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `windows_vm_install_lab_agent.py` first:

```bash
python3 windows_vm_install_lab_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 windows_vm_install_lab_agent.py   # or on stdin
python3 windows_vm_install_lab_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
