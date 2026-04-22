"""Gmail tool appends csm_output_language (ko | inferred) for probes."""

from src.agent.tools.gmail_tool import _annotate_blocks_with_csm_lang, _append_csm_language_footer


def test_korean_subject_gets_ko_footer():
    block = (
        "subject\tRe: [AIQUA] Push 개인화 발송 방식 관련 가이드 미팅 요청\n"
        "from\tSangyoon Park <sangyoon.park@appier.com>\n"
        "\n"
        "Thanks — looping in the team.\n"
    )
    out = _append_csm_language_footer(block)
    assert "csm_output_language\tko" in out
    assert "MANDATORY" in out or "Korean" in out


def test_ascii_subject_gets_inferred_footer():
    block = (
        "subject\tAIQUA API quota question\n"
        "from\tclient@example.com\n"
        "\n"
        "What is the rate limit?\n"
    )
    out = _append_csm_language_footer(block)
    assert "csm_output_language\tinferred" in out
    assert "You decide the language" in out or "primary question" in out


def test_inbox_blob_splits_each_block_separately():
    sep = "\n" + "=" * 60 + "\n"
    kr = "subject\t문의 제목\nfrom\ta@b.com\n\nBody\n"
    en = "subject\tAPI question\nfrom\tc@d.com\n\nBody\n"
    out = _annotate_blocks_with_csm_lang(kr + sep + en)
    assert "csm_output_language\tko" in out
    assert "csm_output_language\tinferred" in out
