# coding=utf-8
from datetime import datetime

"""
Some aggregating functions imported using relfections
"""

"""
AGGREGATORS
Return a dict with some calculated properties. All dicts are combined to form the result.
They are automatically called for "me" and "other" separately. The corresponding postfixes are added automatically.
"""

def aggregator_count(msgs):
    """
    Counts things.
    """
    msg_count = len(msgs)
    word_count = sum(len(msg['text'].split()) for msg in msgs)
    char_count = sum(len(msg['text']) for msg in msgs)
    return {
        'msg_count': msg_count,
        'word_count': word_count,
        'char_count': char_count,
        'words_per_msg': word_count / msg_count,
        'chars_per_msg': char_count / msg_count,
        'chars_per_word': char_count / word_count
    }


def aggregator_active_hours(msgs):
    """
    Counts messages by hour they were sent in
    """
    hours = [0]*24
    for msg in msgs:
        hours[datetime.fromtimestamp(msg['date']).hour] += 1
    return {
        'active_hours': hours
    }


smileys = [
    "😂", "😀", "😬", "😁", "😂", "😃", "😄", "😅", "😆", "😇", "😉", "😊", "🙂", "🙃", "☺️", "😋", "😌", "😍", "😘", "😗", "😙", "😚", "😜", "😝", "😛", "🤑", "🤓", "😎", "🤗", "😏", "😶", "😐", "😑", "😒", "🙄", "🤔", "😳", "😞", "😟", "😠", "😡", "😔", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "😤", "😮", "😱", "😨", "😰", "😯", "😦", "😧", "😢", "😥", "😪", "😓", "😭", "😵", "😲", "🤐", "😷", "🤒", "🤕", "😴", "💤", "💩", "😈", "👿", "👹", "👺", "💀", "👻", "👽", "🤖", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾", "🙌", "👏", "👋", "👍", "👊", "✊", "✌️", "👌", "✋", "💪", "🙏", "☝️", "👆", "👇", "👈", "👉", "🖕", "🤘", "🖖", "✍️", "💅", "👄", "👅", "👂", "👃", "👁", "👀", "👤", "🗣", "👶", "👦", "👧", "👨", "👩", "👱", "👴", "👵", "👲", "👳", "👮", "👷", "💂", "🕵", "🎅", "👼", "👸", "👰", "🚶", "🏃", "💃", "👯", "👫", "👬", "👭", "🙇", "💁", "🙅", "🙆", "🙋", "🙎", "🙍", "💇", "💆", "💑", "👩‍❤️‍👩", "👨‍❤️‍👨", "💏", "👩‍❤️‍💋‍👩", "👨‍❤️‍💋‍👨", "👪", "👨‍👩‍👧", "👨‍👩‍👧‍👦", "👨‍👩‍👦‍👦", "👨‍👩‍👧‍👧", "👩‍👩‍👦", "👩‍👩‍👧", "👩‍👩‍👧‍👦", "👩‍👩‍👦‍👦", "👩‍👩‍👧‍👧", "👨‍👨‍👦", "👨‍👨‍👧", "👨‍👨‍👧‍👦", "👨‍👨‍👦‍👦", "👨‍👨‍👧‍👧", "👚", "👕", "👖", "👔", "👗", "👙", "👘", "💄", "💋", "👣", "👠", "👡", "👢", "👞", "👟", "👒", "🎩", "⛑", "🎓", "👑", "🎒", "👝", "👛", "👜", "💼", "👓", "🕶", "💍", "🌂👴🏻", "👵🏻", "👶🏻", "👱🏻", "👮🏻", "👲🏻", "👳🏻", "👷🏻", "👸🏻", "💂🏻", "🎅🏻", "👼🏻", "💆🏻", "💇🏻", "👰🏻", "🙍🏻", "🙎🏻", "🙅🏻", "🙆🏻", "💁🏻", "🙋🏻", "🙇🏻", "🙌🏻", "🙏🏻", "🚶🏻", "🏃🏻", "💃🏻", "💪🏻", "👈🏻", "👉🏻", "☝️🏻", "👆🏻", "🖕🏻", "👇🏻", "✌️🏻", "🖖🏻", "🤘🏻", "🖐🏻", "✊🏻", "✋🏻", "👊🏻", "👌🏻", "👍🏻", "👎🏻", "👋🏻", "👏🏻", "👐🏻", "✍🏻", "💅🏻", "👂🏻", "👃🏻", "🚣🏻", "🛀🏻", "🏄🏻", "🏇🏻", "🏊🏻", "⛹🏻", "🏋🏻", "🚴🏻", "🚵🏻👦🏼", "👧🏼", "👨🏼", "👩🏼", "👴🏼", "👵🏼", "👶🏼", "👱🏼", "👮🏼", "👲🏼", "👳🏼", "👷🏼", "👸🏼", "💂🏼", "🎅🏼", "👼🏼", "💆🏼", "💇🏼", "👰🏼", "🙍🏼", "🙎🏼", "🙅🏼", "🙆🏼", "💁🏼", "🙋🏼", "🙇🏼", "🙌🏼", "🙏🏼", "🚶🏼", "🏃🏼", "💃🏼", "💪🏼", "👈🏼", "👉🏼", "☝️🏼", "👆🏼", "🖕🏼", "👇🏼", "✌️🏼", "🖖🏼", "🤘🏼", "🖐🏼", "✊🏼", "✋🏼", "👊🏼", "👌🏼", "👍🏼", "👎🏼", "👋🏼", "👏🏼", "👐🏼", "✍🏼", "💅🏼", "👂🏼", "👃🏼", "🚣🏼", "🛀🏼", "🏄🏼", "🏇🏼", "🏊🏼", "⛹🏼", "🏋🏼", "🚴🏼", "🚵🏼👦🏽", "👧🏽", "👨🏽", "👩🏽", "👴🏽", "👵🏽", "👶🏽", "👱🏽", "👮🏽", "👲🏽", "👳🏽", "👷🏽", "👸🏽", "💂🏽", "🎅🏽", "👼🏽", "💆🏽", "💇🏽", "👰🏽", "🙍🏽", "🙎🏽", "🙅🏽", "🙆🏽", "💁🏽", "🙋🏽", "🙇🏽", "🙌🏽", "🙏🏽", "🚶🏽", "🏃🏽", "💃🏽", "💪🏽", "👈🏽", "👉🏽", "☝️🏽", "👆🏽", "🖕🏽", "👇🏽", "✌️🏽", "🖖🏽", "🤘🏽", "🖐🏽", "✊🏽", "✋🏽", "👊🏽", "👌🏽", "👍🏽", "👎🏽", "👋🏽", "👏🏽", "👐🏽", "✍🏽", "💅🏽", "👂🏽", "👃🏽", "🚣🏽", "🛀🏽", "🏄🏽", "🏇🏽", "🏊🏽", "⛹🏽", "🏋🏽", "🚴🏽", "🚵🏽👦🏾", "👧🏾", "👨🏾", "👩🏾", "👴🏾", "👵🏾", "👶🏾", "👱🏾", "👮🏾", "👲🏾", "👳🏾", "👷🏾", "👸🏾", "💂🏾", "🎅🏾", "👼🏾", "💆🏾", "💇🏾", "👰🏾", "🙍🏾", "🙎🏾", "🙅🏾", "🙆🏾", "💁🏾", "🙋🏾", "🙇🏾", "🙌🏾", "🙏🏾", "🚶🏾", "🏃🏾", "💃🏾", "💪🏾", "👈🏾", "👉🏾", "☝️🏾", "👆🏾", "🖕🏾", "👇🏾", "✌️🏾", "🖖🏾", "🤘🏾", "🖐🏾", "✊🏾", "✋🏾", "👊🏾", "👌🏾", "👍🏾", "👎🏾", "👋🏾", "👏🏾", "👐🏾", "✍🏾", "💅🏾", "👂🏾", "👃🏾", "🚣🏾", "🛀🏾", "🏄🏾", "🏇🏾", "🏊🏾", "⛹🏾", "🏋🏾", "🚴🏾", "🚵🏾👦🏿", "👧🏿", "👨🏿", "👩🏿", "👴🏿", "👵🏿", "👶🏿", "👱🏿", "👮🏿", "👲🏿", "👳🏿", "👷🏿", "👸🏿", "💂🏿", "🎅🏿", "👼🏿", "💆🏿", "💇🏿", "👰🏿", "🙍🏿", "🙎🏿", "🙅🏿", "🙆🏿", "💁🏿", "🙋🏿", "🙇🏿", "🙌🏿", "🙏🏿", "🚶🏿", "🏃🏿", "💃🏿", "💪🏿", "👈🏿", "👉🏿", "☝️🏿", "👆🏿", "🖕🏿", "👇🏿", "✌️🏿", "🖖🏿", "🤘🏿", "🖐🏿", "✊🏿", "✋🏿", "👊🏿", "👌🏿", "👍🏿", "👎🏿", "👋🏿", "👏🏿", "👐🏿", "✍🏿", "💅🏿", "👂🏿", "👃🏿", "🚣🏿", "🛀🏿", "🏄🏿", "🏇🏿", "🏊🏿", "⛹🏿", "🏋🏿", "🚴🏿", "🚵🏿🐶", "🐱", "🐭", "🐹", "🐰", "🐻", "🐼", "🐨", "🐯", "🦁", "🐮", "🐷", "🐽", "🐸", "🐙", "🐵", "🙈", "🙉", "🙊", "🐒", "🐔", "🐧", "🐦", "🐤", "🐣", "🐥", "🐺", "🐗", "🐴", "🦄", "🐝", "🐛", "🐌", "🐞", "🐜", "🕷", "🦂", "🦀", "🐍", "🐢", "🐠", "🐟", "🐡", "🐬", "🐳", "🐋", "🐊", "🐆", "🐅", "🐃", "🐂", "🐄", "🐪", "🐫", "🐘", "🐐", "🐏", "🐑", "🐎", "🐖", "🐀", "🐁", "🐓", "🦃", "🕊", "🐕", "🐩", "🐈", "🐇", "🐿", "🐾", "🐉", "🐲", "🌵", "🎄", "🌲", "🌳", "🌴", "🌱", "🌿", "☘", "🍀", "🎍", "🎋", "🍃", "🍂", "🍁", "🌾", "🌺", "🌻", "🌹", "🌷", "🌼", "🌸", "💐", "🍄", "🌰", "🎃", "🐚", "🕸", "🌎", "🌍", "🌏", "🌕", "🌖", "🌗", "🌘", "🌑", "🌒", "🌓", "🌔", "🌚", "🌝", "🌛", "🌜", "🌞", "🌙", "⭐️", "🌟", "💫", "✨", "☄", "☀️", "🌤", "⛅️", "🌥", "🌦", "☁️", "🌧", "⛈", "🌩", "⚡️", "🔥", "💥", "❄️", "🌨", "🔥", "💥", "❄️", "🌨", "☃️", "⛄️", "🌬", "💨", "🌪", "🌫", "☂️", "☔️", "💧", "💦", "🌊🍏", "🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🍈", "🍒", "🍑", "🍍", "🍅", "🍆", "🌶", "🌽", "🍠", "🍯", "🍞", "🧀", "🍗", "🍖", "🍤", "🍳", "🍔", "🍟", "🌭", "🍕", "🍝", "🌮", "🌯", "🍜", "🍲", "🍥", "🍣", "🍱", "🍛", "🍙", "🍚", "🍘", "🍢", "🍡", "🍧", "🍨", "🍦", "🍰", "🎂", "🍮", "🍬", "🍭", "🍫", "🍿", "🍩", "🍪", "🍺", "🍻", "🍷", "🍸", "🍹", "🍾", "🍶", "🍵", "☕️", "🍼", "🍴", "🍽⚽️", "🏀", "🏈", "⚾️", "🎾", "🏐", "🏉", "🎱", "⛳️", "🏌", "🏓", "🏸", "🏒", "🏑", "🏏", "🎿", "⛷", "🏂", "⛸", "🏹", "🎣", "🚣", "🏊", "🏄", "🛀", "⛹", "🏋", "🚴", "🚵", "🏇", "🕴", "🏆", "🎽", "🏅", "🎖", "🎗", "🏵", "🎫", "🎟", "🎭", "🎨", "🎪", "🎤", "🎧", "🎼", "🎹", "🎷", "🎺", "🎸", "🎻", "🎬", "🎮", "👾", "🎯", "🎲", "🎰", "🎳🚗", "🚕", "🚙", "🚌", "🚎", "🏎", "🚓", "🚑", "🚒", "🚐", "🚚", "🚛", "🚜", "🏍", "🚲", "🚨", "🚔", "🚍", "🚘", "🚖", "🚡", "🚠", "🚟", "🚃", "🚋", "🚝", "🚄", "🚅", "🚈", "🚞", "🚂", "🚆", "🚇", "🚊", "🚉", "🚁", "🛩", "✈️", "🛫", "🛬", "⛵️", "🛥", "🚤", "⛴", "🛳", "🚀", "🛰", "💺", "⚓️", "🚧", "⛽️", "🚏", "🚦", "🚥", "🏁", "🚢", "🎡", "🎢", "🎠", "🏗", "🌁", "🗼", "🏭", "⛲️", "🎑", "⛰", "🏔", "🗻", "🌋", "🗾", "🏕", "⛺️", "🏞", "🛣", "🛤", "🌅", "🌄", "🏜", "🏖", "🏝", "🌇", "🌆", "🏙", "🌃", "🌉", "🌌", "🌠", "🎇", "🎆", "🌈", "🏘", "🏰", "🏯", "🏟", "🗽", "🏠", "🏡", "🏚", "🏢", "🏬", "🏣", "🏤", "🏥", "🏦", "🏨", "🏪", "🏫", "🏩", "💒", "🏛", "⛪️", "🕌", "🕍", "🕋", "⛩⌚️", "📱", "📲", "💻", "⌨", "🖥", "🖨", "🖱", "🖲", "🕹", "🗜", "💽", "💾", "💿", "📀", "📼", "📷", "📸", "📹", "🎥", "📽", "🎞", "📞", "☎️", "📟", "📠", "📺", "📻", "🎙", "🎚", "🎛", "⏱", "⏲", "⏰", "🕰", "⏳", "⌛️", "📡", "🔋", "🔌", "💡", "🔦", "🕯", "🗑", "🛢", "💸", "💵", "💴", "💶", "💷", "💰", "💳", "💎", "⚖", "🔧", "🔨", "⚒", "🛠", "⛏", "🔩", "⚙", "⛓", "🔫", "💣", "🔪", "🗡", "⚔", "🛡", "🚬", "☠", "⚰", "⚱", "🏺", "🔮", "📿", "💈", "⚗", "🔭", "🔬", "🕳", "💊", "💉", "🌡", "🏷", "🔖", "🚽", "🚿", "🛁", "🔑", "🗝", "🛋", "🛌", "🛏", "🚪", "🛎", "🖼", "🗺", "⛱", "🗿", "🛍", "🎈", "🎏", "🎀", "🎁", "🎊", "🎉", "🎎", "🎐", "🎌", "🏮", "✉️", "📩", "📨", "📧", "💌", "📮", "📪", "📫", "📬", "📭", "📦", "📯", "📥", "📤", "📜", "📃", "📑", "📊", "📈", "📉", "📄", "📅", "📆", "🗓", "📇", "🗃", "🗳", "🗄", "📋", "🗒", "📁", "📂", "🗂", "🗞", "📰", "📓", "📕", "📗", "📘", "📙", "📔", "📒", "📚", "📖", "🔗", "📎", "🖇", "✂️", "📐", "📏", "📌", "📍", "🚩", "🏳", "🏴", "🔐", "🔒", "🔓", "🔏", "🖊", "🖊", "🖋", "✒️", "📝", "✏️", "🖍", "🖌", "🔍", "🔎❤️", "💛", "💙", "💜", "💔", "❣️", "💕", "💞", "💓", "💗", "💖", "💘", "💝", "💟", "☮", "✝️", "☪", "🕉", "☸", "✡️", "🔯", "🕎", "☯️", "☦", "🛐", "⛎", "♈️", "♉️", "♊️", "♋️", "♌️", "♍️", "♎️", "♏️", "♐️", "♑️", "♒️", "♓️", "🆔", "⚛", "🈳", "🈹", "☢", "☣", "📴", "📳", "🈶", "🈚️", "🈸", "🈺", "🈷️", "✴️", "🆚", "🉑", "💮", "🉐", "㊙️", "㊗️", "🈴", "🈵", "🈲", "🅰️", "🅱️", "🆎", "🆑", "🅾️", "🆘", "⛔️", "📛", "🚫", "❌", "⭕️", "💢", "♨️", "🚷", "🚯", "🚳", "🚱", "🔞", "📵", "❗️", "❕", "❓", "❔", "‼️", "⁉️", "💯", "🔅", "🔆", "🔱", "⚜", "〽️", "⚠️", "🚸", "🔰", "♻️", "🈯️", "💹", "❇️", "✳️", "❎", "✅", "💠", "🌀", "➿", "🌐", "Ⓜ️", "🏧", "🈂️", "🛂", "🛃", "🛄", "🛅", "♿️", "🚭", "🚾", "🅿️", "🚰", "🚹", "🚺", "🚼", "🚻", "🚮", "🎦", "📶", "🈁", "🆖", "🆗", "🆙", "🆒", "🆕", "🆓", "0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟", "🔢", "▶️", "⏸", "⏯", "⏹", "⏺", "⏭", "⏮", "⏩", "⏪", "🔀", "🔁", "🔂", "◀️", "🔼", "🔽", "⏫", "⏬", "➡️", "⬅️", "⬆️", "⬇️", "↗️", "↘️", "↙️", "↖️", "↕️", "↔️", "🔄", "↪️", "↩️", "⤴️", "⤵️", "#️⃣", "*️⃣", "ℹ️", "🔤", "🔡", "🔠", "🔣", "🎵", "🎶", "〰️", "➰", "✔️", "🔃", "➕", "➖", "➗", "✖️", "💲", "💱", "©️", "®️", "™️", "🔚", "🔙", "🔛", "🔝", "🔜", "☑️", "🔘", "⚪️", "⚫️", "🔴", "🔵", "🔸", "🔹", "🔶", "🔷", "🔺", "▪️", "▫️", "⬛️", "⬜️", "🔻", "◼️", "◻️", "◾️", "◽️", "🔲", "🔳", "🔈", "🔉", "🔊", "🔇", "📣", "📢", "🔔", "🔕", "🃏", "🀄️", "♠️", "♣️", "♥️", "♦️", "🎴", "👁‍🗨", "💭", "🗯", "💬", "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛", "🕜", "🕝", "🕞", "🕟", "🕠", "🕡", "🕢", "🕣", "🕤", "🕥", "🕦", "🕧", "🤣", "🤠", "🤡", "🤥", "🤤", "🤢", "🤧", "🤴", "🤶", "🤵", "🤷", "🤦", "🤰", "🕺", "🤳", "🤞", "🤙", "🤛", "🤜", "🤚", "🤝", "🖤", "🦍", "🦊", "🦌", "🦏", "🦇", "🦅", "🦆", "🦉", "🦎", "🦈", "🦐", "🦑", "🦋", "🥀", "🥝", "🥑", "🥔", "🥕", "🥒", "🥜", "🥐", "🥖", "🥞", "🥓", "🥙", "🥚", "🥘", "🥗", "🥛", "🥂", "🥃", "🥄", "🛑", "🛴", "🛵", "🛶", "🥇", "🥈", "🥉", "🥊", "🥋", "🤸", "🤼", "🤽", "🤾", "🤺", "🥅", "🤹", "🥁", "🛒", "☺️", "☹", "☝️", "✌️", "✍️", "❤️", "❣️", "☠", "♨️", "✈️", "⌛", "⌚", "♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓", "☀️", "☁️", "☂️", "❄️", "⛄️", "☄", "♠️", "♥️", "♦️", "♣️", "▶️", "◀️", "☎️", "⌨", "✉️", "✏️", "✒️", "✂️", "↗️", "➡️", "↘️", "↙️", "↖️", "↕️", "↔️", "↩️", "↪️", "✡️", "☸", "☯️", "✝️", "☦", "☪", "☮", "☢", "☣", "☑️", "✔️", "✖️", "✳️", "✴️", "❇️", "‼️", "©️", "®️", "™️", "Ⓜ️", "▪️", "▫️", "#⃣️", "*️⃣", "0⃣️", "1⃣️", "2⃣️", "3⃣️", "4⃣️", "5⃣️", "6⃣️", "7⃣️", "8⃣️", "9⃣️", "⁉️", "ℹ️", "⤴️", "⤵️", "♻️", "◻️", "◼️", "◽", "◾", "☕", "⚠️", "☔", "⏏", "⬆️", "⬇️", "⬅️", "⚡", "☘", "⚓", "♿", "⚒", "⚙", "⚗", "⚖", "⚔", "⚰", "⚱", "⚜", "⚛", "⚪", "⚫", "🀄", "⭐", "⬛", "⬜", "⛑", "⛰", "⛪", "⛲", "⛺", "⛽", "⛵", "⛴", "⛔", "⛅", "⛈", "⛱", "⛄", "⚽", "⚾️", "⛳", "⛸", "⛷", "⛹", "⛏", "⛓", "⛩", "⭕", "❗", "🅿️", "❦", "♕", "♛", "♔", "♖", "♜", "☾", "→", "⇒", "⟹", "⇨", "⇰", "➩", "➪", "➫", "➬", "➭", "➮", "➯", "➲", "➳", "➵", "➸", "➻", "➺", "➼", "➽", "☜", "☟", "➹", "➷", "↶", "↷", "✆", "⌘", "⎋", "⏎", "⏏", "⎈", "⎌", "⍟", "❥", "ツ", "ღ", "☻", ">:(", ">:O", "<3", "(^^^)", "(y)", "-_-", "3:)", "8-)", "8|", ":'(", ":(", ":-(", ":)", ":-)", ":*", ":/", ":3", ":D", ":-D", ":O", ":P", ":poop:", ":putnam:", ":v", ":|]", ";)", "<(\")", "^_^", "o.O", "O:)"
]


def aggregator_smileys(msgs):
    """
    Counts smileys, both unicode and ASCII
    """
    count = {smiley: sum([m["text"].count(smiley) for m in msgs]) for smiley in smileys}
    total = sum(count.values())
    return {
        'smiley_count': {smiley: count[smiley] for smiley in smileys if count[smiley] > 0},
        'total_smileys': total,
        'smileys_per_message': total / len(msgs)
    }


def aggregator_active_days(msgs):
    """
    Finds the day of the first and last message detected
    """
    date_first_message = msgs[-1]['date']
    date_last_message = msgs[0]['date']
    return {
        'date_first_message': date_first_message,
        'date_last_message': date_last_message
    }

"""
DUAL AGGREGATORS
Just like regual aggregators, but called with mixed "me" and "other" messages.
"""

conv_delay = 600


def dual_aggregator_conversations(msgs):
    """
    Breaks messages into "conversations" (blocks of messages with the maximum delay lower than conv_delay)
    This makes computing avg_message_delay much more accurate
    """
    rmsgs = list(reversed(msgs))
    conversations_count = 0
    conversations_time = 0
    start = rmsgs[0]
    last = start
    for i in range(1, len(rmsgs)):
        if rmsgs[i]['date'] > (last['date'] + conv_delay):
            if start != last:  # Don't count 1-message conversations
                conversations_count += 1
                conversations_time += last['date'] - start['date']
            start = rmsgs[i]
            last = start
        else:
            last = rmsgs[i]
    return {
        'conversations_count': conversations_count,
        'total_conversations_time': conversations_time,
        'avg_conversation_time': conversations_time / conversations_count,
        'avg_message_delay': conversations_time / len(msgs)
    }


def dual_aggregator_questions(msgs):
    """
    Dectects questions and counts the average time to respond
    """
    rmsgs = list(reversed(msgs))
    last_question = None
    question_waiting_time = [0, 0]
    questions_count = [0, 0]
    for i in range(len(rmsgs)):
        if last_question is not None and last_question['by_me'] != rmsgs[i]['by_me']:
            question_waiting_time[+rmsgs[i]['by_me']] += min(rmsgs[i]['date'] - last_question['date'], 3600*12)
            questions_count[+rmsgs[i]['by_me']] += 1
        last_question = rmsgs[i] if rmsgs[i]['text'].endswith("?") else None
    return {
        'avg_response_delay_other': question_waiting_time[0] / questions_count[0],
        'avg_response_delay_me': question_waiting_time[1] / questions_count[1]
    }

"""
POSTPROCESSORS
They are called at the very last, on the resulting "data" object. They may edit it as they please.
"""


def postprocessor_message_ratio(data):
    for k, d in data.items():
        if k.startswith("_"):
            continue
        d['msg_ratio_me'] = d['msg_count_me'] / (d['msg_count_other'] + d['msg_count_me'])
        d['word_ratio_me'] = d['word_count_me'] / (d['word_count_other'] + d['word_count_me'])
        d['char_ratio_me'] = d['char_count_me'] / (d['char_count_other'] + d['char_count_me'])


# This one is cool for manual analysis, but doesn't really make sense and breaks plotting
"""
def postprocessor_records(data):
    firstitem = next(iter(data.values()))
    disciplines = [k for k in firstitem.keys() if isinstance(firstitem[k], (int, float))]
    maximums = {d: None for d in disciplines}
    minimums = {d: None for d in disciplines}
    for k, d in data.items():
        if k.startswith("_"):
            continue
        for discipline in disciplines:
            if maximums[discipline] is None or d[discipline] > data[maximums[discipline]][discipline]:
                maximums[discipline] = k
            if minimums[discipline] is None or d[discipline] < data[minimums[discipline]][discipline]:
                minimums[discipline] = k
    data['_RECORDS'] = {'max': maximums, 'min': minimums}
"""
