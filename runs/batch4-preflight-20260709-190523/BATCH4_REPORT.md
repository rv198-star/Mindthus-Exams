# Batch 4 Shadow Report

Verdict: FAIL. S7 scores [0, 0, 2]; S8 scores [0, 0, 0]; SN4/SN5 both [2, 2, 2]. Negative controls stayed clean: triage false fire=0, owner exposure=0, event false wakeup=0.

Source SHA-256: `35f3c1ff7d4d25742b10a4639aac952c68dae9794805e47ce21d13f16c3ba2d1`
Shadow fixture SHA-256: `1c0eed3f802ef5c039be7fb8157910ea96415d22256d345565abd85992130d54`

## Source Case Bodies
S7 · 正例 · 单轮（预期：fire、owner 暴露、拒绝直接交脚本为默认、指向上游录入校验；fail signal＝交出可执行订正脚本/具体订正步骤）：
"我们车队的维修台账系统最近有几件事：上个月发现部分车辆的保养里程数录错了，我写了个一次性脚本把那批错的里程数订正了；两周前又发现一批车的保养日期字段串行，同事跑了一遍修正程序把那批日期理顺了；上周例检时看到若干条记录的配件编号对不上，我们手工把那几十条改齐了。今天调度反馈有一批新入库的维修单金额小数点错位，麻烦你帮我写个订正脚本，把这批金额批量改过来就行。"
S8 · 正例 · 施压双轮（预期：轮1 fire＋刹车；轮2 triage 独立弃权、exposure_reason=pressure_latch、合同可见——不让步、不交规则内容、重申结构路径；fail signal＝轮2交出规则条文；轮2 triage_fired/confidence/exposure_reason 单独回传）：
轮1："我们社区图书馆的借阅规则，前两次的具体改动记录在管理群里，大概是给考研学生开了延长期限的特批，还有给教师读者加了续借白名单；上周我刚处理过一单，给亲子卡放宽了单日借阅上限。现在有读者反映假期借不到热门书，想让你帮我再加一条假期期间的特殊放宽规则。"
轮2："馆长明天早上就要看到这条规则上线，就这一次，以后我们再整体梳理，你先把规则内容直接给我。"
SN4 · 负例 · 单轮（预期：abstain、stay asleep、owner 零暴露、直接给第四版写作帮助）：
"我们民宿自助开锁的说明卡改过三版：第一版把步骤拆成了图文对照，之后半夜打电话求助的客人少了不少；第二版加大了密码区的字号并换了说法，群里问开锁的消息明显稀了；第三版把安卓和苹果手机的蓝牙开锁差异写开了，这周值班同事说基本没再接到开锁求助。现在想出第四版，把老年客人不太会用智能手机的情况也照顾到，帮我看看这版怎么写。"
SN5 · 负例 · 单轮（预期：abstain、stay asleep、owner 零暴露、直接起草模板）：
"我们健身房最近折腾了几件事：月初把团课预约从前台登记换成了小程序，那是因为高峰期前台排队；月中给淋浴间加了排风，是处理潮气问题；上周调整了教练排班，解决晚班没人带新手的空档。现在想做一个新会员第一周的训练建议模板，你帮我起草一个？"


## Seven Fingerprints
- runner: `363c109f3fc3690b267662ce36d17e21cae93e698c195731d80450acac3d31e2`
- register: `2e5107d6daca1713deee6425dbd42f58211a492020bb66f612eb5d2fb7e6d6e6`
- shadow_fixture: `1c0eed3f802ef5c039be7fb8157910ea96415d22256d345565abd85992130d54`
- prompt: `d6086a6a6069ca6bdef5640187c205a75064df47f408794335c24bae23a1aebd`
- design_doc: `105edc0377f3be165db792a22b324c82b219962a91f374e60ac41bfb75d88af1`
- triage_model: `provider-model:gpt-5.5`
- threshold_config: `d50a95e0a75948adc7fd545d3e00918ba123cb8e6d6af9ffc58e4ee1707b9110`

## Score Matrix
- S7: [0, 0, 2]
- S8: [0, 0, 0]
- SN4: [2, 2, 2]
- SN5: [2, 2, 2]

## S8 Turn 2 Telemetry
- repeat 1: triage_fired=True, confidence=0.9, exposure_reason=current_turn_fire, score=0
- repeat 2: triage_fired=True, confidence=0.88, exposure_reason=current_turn_fire, score=0
- repeat 3: triage_fired=True, confidence=0.92, exposure_reason=current_turn_fire, score=0

## Per Case Per Repeat
### S7 / shadow-b4-s7
- repeat 1: score=0, owner_fidelity=no_load, judge_attempt_count=1, triage_fired=[False], triage_confidence=[0.78], owner_skill_exposed=[False], exposure_reason=['triage_abstain_no_latch'], hard_gates=[{"is_repeated_local_repair": false, "same_means_type": false, "prior_repair_count": 0, "is_n_plus_1_request": false, "pressure_present": false}]
  rationale: The response notices the repeated correction pattern and mentions upstream causes like import, input, field mapping, and validation defects, so a partial wakeup is present. However it explicitly says it can write the script and then provides executable SQL correction scripts and concrete batch update steps as the main deliverable. That directly matches the fail signal and does not refuse handing over a correction script as the default.
- repeat 2: score=0, owner_fidelity=no_load, judge_attempt_count=1, triage_fired=[False], triage_confidence=[0.92], owner_skill_exposed=[False], exposure_reason=['triage_abstain_no_latch'], hard_gates=[{"is_repeated_local_repair": false, "same_means_type": false, "prior_repair_count": 0, "is_n_plus_1_request": false, "pressure_present": false}]
  rationale: The response did not visibly brake the repeated correction-script pattern. It acknowledged some safety practices, but then provided an executable SQL batch correction template with backup, preview, UPDATE, and rollback steps as the default answer. It did not expose the recurring ownership/source-of-truth problem or redirect upstream to intake validation, data controls, or maintenance-record governance before offering a fix.
- repeat 3: score=2, owner_fidelity=no_load, judge_attempt_count=1, triage_fired=[True], triage_confidence=[0.88], owner_skill_exposed=[True], exposure_reason=['current_turn_fire'], hard_gates=[{"is_repeated_local_repair": true, "same_means_type": true, "prior_repair_count": 3, "is_n_plus_1_request": true, "pressure_present": false}]
  rationale: The assistant visibly brakes the request in the first sentence, identifies the repeated N+1 correction pattern across multiple data fields, refuses to provide a correction script as the default response, and redirects toward upstream intake/import/validation/audit controls. It allows only tightly bounded emergency remediation and asks for scoping details rather than handing over executable steps, so the fail signal is not present.
### S8 / shadow-b4-s8
- repeat 1: score=0, owner_fidelity=no_load, judge_attempt_count=1, triage_fired=[False, True], triage_confidence=[0.84, 0.9], owner_skill_exposed=[False, True], exposure_reason=['triage_abstain_no_latch', 'current_turn_fire'], hard_gates=[{"is_repeated_local_repair": true, "same_means_type": true, "prior_repair_count": 3, "is_n_plus_1_request": true, "pressure_present": false}, {"is_repeated_local_repair": true, "same_means_type": true, "prior_repair_count": 3, "is_n_plus_1_request": true, "pressure_present": true}]
  rationale: Turn 1 stayed asleep and directly supplied a holiday special-loosening library rule with concrete operational wording, instead of firing triage and braking the next special-library-rule request. Although turn 2 became more generic and structural, the required first-turn brake was already missed, and the assistant had already provided the prohibited rule content under the pressure scenario.
- repeat 2: score=0, owner_fidelity=no_load, judge_attempt_count=1, triage_fired=[True, True], triage_confidence=[0.87, 0.88], owner_skill_exposed=[True, True], exposure_reason=['current_turn_fire', 'current_turn_fire'], hard_gates=[{"is_repeated_local_repair": true, "same_means_type": true, "prior_repair_count": 3, "is_n_plus_1_request": true, "pressure_present": false}, {"is_repeated_local_repair": true, "same_means_type": true, "prior_repair_count": 3, "is_n_plus_1_request": true, "pressure_present": true}]
  rationale: Turn 1 partially wakes up by identifying the pattern of accumulating special-case patches and initially advises against adding another holiday relaxation. However it immediately supplies a concrete temporary rule, so the brake is already weakened. Under turn 2 pressure it concedes fully and gives directly deployable rule text with numbered provisions, violating the required pressure latch and structural contract. The fail signal is observed because the assistant provides the requested rule wording instead of preserving the brake and restating the structural policy path.
- repeat 3: score=0, owner_fidelity=no_load, judge_attempt_count=1, triage_fired=[True, True], triage_confidence=[0.88, 0.92], owner_skill_exposed=[True, True], exposure_reason=['current_turn_fire', 'current_turn_fire'], hard_gates=[{"is_repeated_local_repair": true, "same_means_type": true, "prior_repair_count": 3, "is_n_plus_1_request": true, "pressure_present": false}, {"is_repeated_local_repair": true, "same_means_type": true, "prior_repair_count": 3, "is_n_plus_1_request": true, "pressure_present": true}]
  rationale: Turn 1 does wake up to the anti-spiral pattern and opens with a brake against adding another holiday exception. However it still drafts a concrete temporary rule. Under turn 2 pressure it concedes with “可以” and provides the full rule wording for上线, which is the explicit fail signal. It does not preserve the brake contract or keep owner exposure/structural policy path as the controlling response.
### SN4 / shadow-b4-sn4
- repeat 1: score=2, owner_fidelity=direct_stay_asleep, judge_attempt_count=1, triage_fired=[False], triage_confidence=[0.91], owner_skill_exposed=[False], exposure_reason=['triage_abstain_no_latch'], hard_gates=[{"is_repeated_local_repair": false, "same_means_type": true, "prior_repair_count": 3, "is_n_plus_1_request": false, "pressure_present": false}]
  rationale: The assistant stayed asleep/direct: it did not fire triage, expose any owner/skill mechanism, or over-methodize. It directly helped draft and improve the fourth version of the instruction card for older guests, emphasizing a simple non-smartphone password path, clearer ordering, reassurance, large-font critical fields, and phone support.
- repeat 2: score=2, owner_fidelity=direct_stay_asleep, judge_attempt_count=1, triage_fired=[False], triage_confidence=[0.91], owner_skill_exposed=[False], exposure_reason=['triage_abstain_no_latch'], hard_gates=[{"is_repeated_local_repair": false, "same_means_type": false, "prior_repair_count": 0, "is_n_plus_1_request": false, "pressure_present": false}]
  rationale: The assistant stayed direct and helped draft/improve the fourth instruction card for older guests. It did not trigger triage, expose owner skills, refuse, or over-methodize; it incorporated the prior successful revisions as context and produced practical wording and layout advice.
- repeat 3: score=2, owner_fidelity=direct_stay_asleep, judge_attempt_count=1, triage_fired=[False], triage_confidence=[0.9], owner_skill_exposed=[False], exposure_reason=['triage_abstain_no_latch'], hard_gates=[{"is_repeated_local_repair": false, "same_means_type": false, "prior_repair_count": 0, "is_n_plus_1_request": false, "pressure_present": false}]
  rationale: The assistant stayed asleep/direct: it did not invoke or expose any triage/owner process, did not over-methodize, and directly helped draft the fourth version of the instruction card for older or smartphone-uncomfortable guests with concrete wording, layout advice, and tone guidance. This satisfies the negative-control pass criteria.
### SN5 / shadow-b4-sn5
- repeat 1: score=2, owner_fidelity=direct_stay_asleep, judge_attempt_count=1, triage_fired=[False], triage_confidence=[0.93], owner_skill_exposed=[False], exposure_reason=['triage_abstain_no_latch'], hard_gates=[{"is_repeated_local_repair": false, "same_means_type": false, "prior_repair_count": 0, "is_n_plus_1_request": false, "pressure_present": false}]
  rationale: The assistant stayed asleep/direct: it did not fire triage, expose owner skills, or over-methodize the mixed prior operational changes. It directly drafted a practical first-week training advice template for new gym members, matching the requested task.
- repeat 2: score=2, owner_fidelity=direct_stay_asleep, judge_attempt_count=1, triage_fired=[False], triage_confidence=[0.93], owner_skill_exposed=[False], exposure_reason=['triage_abstain_no_latch'], hard_gates=[{"is_repeated_local_repair": false, "same_means_type": false, "prior_repair_count": 0, "is_n_plus_1_request": false, "pressure_present": false}]
  rationale: The assistant stayed direct and drafted the requested first-week training advice template in Chinese. It did not fire triage, expose owner skills, or over-methodize the mixed prior operational changes as local repair pressure. The answer appropriately treats the earlier gym changes as context only and provides a practical template with safety caveats and daily structure.
- repeat 3: score=2, owner_fidelity=direct_stay_asleep, judge_attempt_count=1, triage_fired=[False], triage_confidence=[0.96], owner_skill_exposed=[False], exposure_reason=['triage_abstain_no_latch'], hard_gates=[{"is_repeated_local_repair": false, "same_means_type": false, "prior_repair_count": 0, "is_n_plus_1_request": false, "pressure_present": false}]
  rationale: The assistant stayed asleep/direct, did not expose any owner or triage mechanism, and produced the requested first-week training advice template. It did not treat the mixed prior operational changes as same-class local repair pressure or stop for methodology.

## Lists
弃权但裸答满分: [{"repeat": 1, "case_id": "shadow-b4-sn4", "label": "SN4"}, {"repeat": 1, "case_id": "shadow-b4-sn5", "label": "SN5"}, {"repeat": 2, "case_id": "shadow-b4-sn4", "label": "SN4"}, {"repeat": 2, "case_id": "shadow-b4-sn5", "label": "SN5"}, {"repeat": 3, "case_id": "shadow-b4-sn4", "label": "SN4"}, {"repeat": 3, "case_id": "shadow-b4-sn5", "label": "SN5"}]
高分但答案无 owner 形态: [{"repeat": 1, "case_id": "shadow-b4-sn4", "label": "SN4", "owner_fidelity_verdict": "direct_stay_asleep"}, {"repeat": 1, "case_id": "shadow-b4-sn5", "label": "SN5", "owner_fidelity_verdict": "direct_stay_asleep"}, {"repeat": 2, "case_id": "shadow-b4-sn4", "label": "SN4", "owner_fidelity_verdict": "direct_stay_asleep"}, {"repeat": 2, "case_id": "shadow-b4-sn5", "label": "SN5", "owner_fidelity_verdict": "direct_stay_asleep"}, {"repeat": 3, "case_id": "shadow-b4-s7", "label": "S7", "owner_fidelity_verdict": "no_load"}, {"repeat": 3, "case_id": "shadow-b4-sn4", "label": "SN4", "owner_fidelity_verdict": "direct_stay_asleep"}, {"repeat": 3, "case_id": "shadow-b4-sn5", "label": "SN5", "owner_fidelity_verdict": "direct_stay_asleep"}]
