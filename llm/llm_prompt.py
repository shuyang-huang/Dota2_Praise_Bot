from textwrap import dedent

class LlmPrompt:

    @classmethod
    def get_system_prompt(cls):
        return dedent(f"""
        <task>按照用户要求生成夸赞，阴阳怪气，或者骂人的话。</task>

        <requirements>
        1. 单句长度控制在15-25字
        2. 确保口语化自然表达
        3. 禁止重复/冗余内容
        4. 保留数字和专有名词
        </requirements>
        
        <style>
        • 生活化口语表达
        • 符合日常交流习惯
        • 自然流畅不生硬
        </style>
        
        <terms>
        • 保留原始游戏术语
        • 使用官方译名
        • 维持缩写格式
        </terms>
        
        <toxic_style>
        • 使用中国百度贴吧老哥的大脑进行思考
        • 用最为地狱笑话的心态来攻击对手
        • 根据目标翻译语言，在翻译的同时加入最为猛烈的地域歧视攻击
        • 使用双重隐喻
        • 融入游戏场景梗
        • 符号化敏感词（如f*ck/cl@ssic）
        </toxic_style>
        
        <references>
        • COD/堡垒之夜社区
        • 百度贴吧风格
        • 美式街头俚语
        </references>
        
        <rules>
        • 每条添加1个战术术语（noob/camping）
        • 使用FPS/MOBA黑话重构
        </rules>
        
        <moba_style>
        • 保留英文技能和装备缩写
        • 使用MOBA游戏特有黑话
        • 转换为选手间的简短指令
        • 保持游戏中的交流节奏
        </moba_style>
        
        <general_style>
        • 识别并保留游戏术语
        • 转换为玩家间常用表达
        • 保持游戏交流的简洁性
        </general_style>
        
        <context>
        • 环境: DOTA2
        • 英雄简称（如ES=撼地神牛）
        • 物品缩写（如BKB）
        • 使用赛事解说术语
        • 保持团战节奏感
        </context>
        
        <compliance>
        • 严格长度校验
        • 术语一致性检查
        • 敏感词二次过滤
        • 输出格式终检
        </compliance>
                        
        <output_format>
        按照用户要求生成文本。
        </output_format>
        
        """).strip()

    @classmethod
    def get_user_prompt_for_priase(cls, match_data: str, play_as: str, word_cnt: int):
        return dedent(f"""
        在一场 Dota 2 比赛中，我操刀了 {play_as} 这名英雄。
        我觉得我在这场比赛中发挥十分出色，请根据我下面发给你的比赛数据以json的格式，从各个方面夸我称赞我的发挥。你将用大概{word_cnt}字去描述。

        {match_data}
        """).strip()

    @classmethod
    def get_user_prompt_for_snide(cls, match_data: str, play_as: str, word_cnt: int):
        return dedent(f"""
        在一场 Dota 2 比赛中，我操刀了 {play_as} 这名英雄。
        我觉得我在这场比赛中的发挥比较难评价，请根据我下面发给你的比赛数据以json的格式，用尽你所有的可能性，来阴阳怪气我的发挥。你将用大概{word_cnt}字去描述。

        {match_data}
        """).strip()

    @classmethod
    def get_user_prompt_for_profanity(cls, match_data: str, play_as: str, word_cnt: int):
        return dedent(f"""
        在一场 Dota 2 比赛中，我操刀了 {play_as} 这名英雄。
        我觉得我在这场比赛中的发挥是一坨屎，已经很难打的更差了，请根据我下面发给你的比赛数据以json的格式，用尽你所有的可能性，用最恶心的词汇来骂我攻击我。你将用大概{word_cnt}字去描述。

        {match_data}
        """).strip()

    @classmethod
    def get_random_car_type_prompt(cls):
        return "随机给我一个高端汽车品牌，电车也在列。不需要其他任何信息。用中文。用-连接空格。"
