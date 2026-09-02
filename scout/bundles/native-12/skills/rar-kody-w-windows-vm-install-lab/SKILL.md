---
name: "rar-kody-w-windows-vm-install-lab"
description: "Runs an allowlisted Hyper-V Windows 11 lab for repeatable RAPP installer release testing with an embedded, hash-verified toolkit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/windows_vm_install_lab_agent", "rar_sha256": "cb3249f0118aa4edf62f99daa353c1fa9ad50c79684832158351cdf81b9ca1bb", "source_kind": "rar-agent", "source_commit": "078c9f76011af965f40983af7f225debec8e76b8", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "windows_vm_install_lab_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/windows-vm-install-lab:957aac89deb34b545af7bdf0e483ca4fb2c3ecca74155ce2e34d6919fa3da832", "kind": "skill"}, "author": "RAPP Community", "tags": ["windows", "hyper-v", "installer", "testing", "automation"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/windows_vm_install_lab_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `windows_vm_install_lab_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
